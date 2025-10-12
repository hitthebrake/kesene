import requests

from django.core.cache import cache
from django.conf import settings
from django.db import connection
from django.utils import timezone

from monitoring.services.scenario import ScenarioCheck
from sensors.models import SensorSettings, ScenarioInstance
from webhook.sensor_parsing import get_sensor_types
from webhook.models import Sensor, MeteoData


def wind_direction_sign(degrees: float) -> str:
    degrees = degrees % 360

    if 337.5 <= degrees or degrees < 22.5:
        return "С"
    elif 22.5 <= degrees < 67.5:
        return "С-В"
    elif 67.5 <= degrees < 112.5:
        return "В"
    elif 112.5 <= degrees < 157.5:
        return "Ю-В"
    elif 157.5 <= degrees < 202.5:
        return "Ю"
    elif 202.5 <= degrees < 247.5:
        return "Ю-З"
    elif 247.5 <= degrees < 292.5:
        return "З"
    elif 292.5 <= degrees < 337.5:
        return "С-З"
    return ""


def check_limits(setting, value):

    if setting.from_value is None and setting.to_value is None and value == "#NV":
        return True
    if (setting.from_value is None and setting.to_value is None) or value == "#NV":
        return False

    if float(setting.from_value) < float(value) <= float(setting.to_value):
        return True
    return False


def compare_status(value1, value2):
    priorities = {
        'Норма': 0,
        'Нет данных': 1,
        'Предупреждение': 2,
        'Тревога': 3
    }
    return value1 if priorities.get(value1, 0) > priorities.get(value2, 0) else value2


class LatestData(ScenarioCheck):
    def get_data(self):
        latest_values = self.get_latest_measurements()
        latest_local_meteo = self.get_latest_local_meteo_data()
        latest_api_meteo = self.get_latest_api_meteo_data()
        scenarios = self.scenario_check(latest_values, latest_api_meteo)
        resolved_scenarios = ScenarioInstance.objects.filter(triggered_at=timezone.now().date(), status='resolved')
        return {
            'latest_values': latest_values,
            'latest_local_meteo': latest_local_meteo,
            'latest_api_meteo': latest_api_meteo,
            'scenarios': scenarios,
            'resolved_scenarios': resolved_scenarios,
        }

    @staticmethod
    def get_latest_measurements():
        sensors = Sensor.objects.all()
        with connection.cursor() as cursor:
            cursor.execute("""
                           SELECT s.sensor_id, m.value1, m.value2, m.value3
                           FROM (SELECT DISTINCT sensor_id
                                 FROM webhook_measurement) AS s
                                    CROSS JOIN LATERAL (
                               SELECT value1, value2, value3
                               FROM webhook_measurement m
                               WHERE m.sensor_id = s.sensor_id
                               ORDER BY m.date DESC
                               LIMIT 1
                               ) AS m;
                           """)
            raw_rows = cursor.fetchall()

        latest_values = {}
        for sensor in sensors:
            for sensor_id, value1, value2, value3 in raw_rows:
                if sensor_id == sensor.id:
                    latest_values[sensor_id] = {
                        'value1': value1 if value1 is not None else '#NV',
                        'value2': value2 if value2 is not None else '#NV',
                        'value3': value3 if value3 is not None else '#NV',
                        'spot': sensor.spot,
                        'name': sensor.name,
                        'location': sensor.location,
                        'sensor_type': sensor.sensor_type,
                        'setting': {'status': 'Норма'},
                        'sensor_image': sensor.image
                    }
                    sensor_types = get_sensor_types(sensor.sensor_type)
                    sensor_settings = SensorSettings.objects.filter(sensor_id=sensor_id)
                    for i in range(len(sensor_types)):
                        latest_values[sensor_id][f'type{i + 1}'] = sensor_types[i][1]
                        for s in sensor_settings:
                            if s.type_name == sensor_types[i][0]:
                                if check_limits(s, latest_values[sensor_id][f'value{i+1}']):
                                    status = compare_status(latest_values[sensor_id]['setting']['status'], s.status)
                                    if status == s.status:
                                        latest_values[sensor_id]['setting'] = {
                                            'status': s.status,
                                            'id': s.id,
                                            'action': s.action,
                                        }

        return latest_values

    @staticmethod
    def get_latest_local_meteo_data():
        try:
            last_instance = MeteoData.objects.latest('date')
            return {
                'date': last_instance.date,
                'temperature': last_instance.temperature,
                'dewpoint': last_instance.dewpoint,
                'pressure': last_instance.pressure,
                'humidity': last_instance.humidity,
                'wind_speed': last_instance.wind_speed,
                'wind_direction': round(last_instance.wind_direction),
                'precipitation': last_instance.precipitation,
                'wind_direction_sign': wind_direction_sign(float(last_instance.wind_direction)),
            }
        except MeteoData.DoesNotExist:
            return {}


    @staticmethod
    def get_weather():
        cache_key = "weather_data"
        data = cache.get(cache_key)

        if not data:  # no cache or expired
            response = requests.get(
                f"https://api.openweathermap.org/data/3.0/onecall?lat=43.2975&lon=68.2708&exclude=hourly,alerts&appid={settings.WEATHER_API_KEY}")  # your weather API
            if response.status_code == 200:
                data = response.json()
                cache.set(cache_key, data, timeout=360)  # cache for 360 seconds (6 minutes)
            else:
                data = {"error": "Failed to fetch weather"}
        return data

    def get_latest_api_meteo_data(self):
        data = self.get_weather()
        if data.get("error", ''):
            return data
        try:
            return {
                'temperature': round(data['current']['temp']-273, 2),
                'dewpoint': round(data['current']['dew_point']-273, 2),
                'pressure': data['current']['pressure'],
                'humidity': data['current']['humidity'],
                'wind_speed': data['current']['wind_speed'],
                'wind_direction': round(data['current']['wind_deg']),
                'precipitation': data['minutely'][0]['precipitation'],
                'wind_direction_sign': wind_direction_sign(data['current']['wind_deg']),
            }
        except Exception as e:
            return {}


