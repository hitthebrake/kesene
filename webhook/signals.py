from datetime import datetime

from django.db.models.signals import post_save
from django.dispatch import receiver

from webhook.models import WebhookRequest, Sensor, Measurement, MeteoData
from webhook.sensor_parsing import get_sensor_info, parse_dt, safe_float
from reports.extra_functions import format_date

from webhook.models import Sensor, Measurement, MeteoData



@receiver(post_save, sender=WebhookRequest, dispatch_uid='data_saved')
def data_saved(sender, instance, created, **kwargs):
    print('Signal fired!!!')
    if created:
        existing_sensors = list(
            Sensor.objects.all().values_list('name', 'location', 'spot', 'sensor_type', 'id')
        )
        existing_measurements = [
            (str(date), safe_float(v1), safe_float(v2), safe_float(v3), sensor)
            for date, v1, v2, v3, sensor in Measurement.objects
            .values_list('date', 'value1', 'value2', 'value3', 'sensor_id')
        ]
        existing_meteo_data = list(
            (str(date), safe_float(v1), safe_float(v2), safe_float(v3), safe_float(v4), safe_float(v5),
            safe_float(v6), safe_float(v7))
            for date, v1, v2, v3, v4, v5, v6, v7 in MeteoData.objects.values_list(
            'date', 'temperature', 'dewpoint', 'pressure', 'humidity', 'wind_speed',
            'wind_direction', 'precipitation')
        )

        instances_to_create = []
        meteo_instances_to_create = []
        sheets = instance.data['sheets']

        for key, value in sheets.items():
            sensor_data = get_sensor_info(key)
            if len(sensor_data) == 0:
                continue

            # handling Meteo data
            if sensor_data['name'] == 'Метео данные':
                value[0] = str(format_date(parse_dt(value[0])))
                for i in range(1, len(value)):
                    value[i] = 100000 if value[i] == "#NV" else value[i]
                    if value[i] > 10000 or value[i] < -10000:
                        value[i] = None

                if tuple(value) not in existing_meteo_data:
                    date, temperature, dewpoint, pressure, humidity, wind_speed, wind_direction, precipitation = value
                    obj = MeteoData(
                        date=date,
                        temperature=temperature,
                        dewpoint=dewpoint,
                        pressure=pressure,
                        humidity=humidity,
                        wind_speed=wind_speed,
                        wind_direction=wind_direction,
                        precipitation=precipitation,
                    )
                    meteo_instances_to_create.append(obj)
                    existing_meteo_data.append(tuple(value))
                    print('meteo created')
                continue

            # creates sensor
            if not (sensor_data['name'], sensor_data['location'], sensor_data['spot'],
                    sensor_data['type']) in existing_sensors:
                Sensor.objects.get_or_create(
                    name=sensor_data['name'],
                    location=sensor_data['location'],
                    spot=sensor_data['spot'],
                    sensor_type=sensor_data['type'],
                )
                existing_sensors = list(
                    Sensor.objects.all().values_list('name', 'location', 'spot', 'sensor_type', 'id')
                )

            date, *measurement_values = value
            dt = str(format_date(parse_dt(date)))
            values = [100000, 100000, 100000]

            for i in range(len(measurement_values)):
                values[i] = 100000 if measurement_values[i] == "#NV" else measurement_values[i]
            for i in range(3):
                if values[i] > 10000 or values[i] < -10000:
                    values[i] = None

            # find sensor id
            sensor_id = None
            for sensor in existing_sensors:
                if (sensor_data['name'], sensor_data['location'], sensor_data['spot'], sensor_data['type']) == sensor[:4]:
                    sensor_id = sensor[4]

            # create measurement if it does not exist
            if not (dt, values[0], values[1], values[2], sensor_id) in existing_measurements:
                obj = Measurement(
                    date=dt, value1=values[0], value2=values[1], value3=values[2], sensor_id=sensor_id,
                )
                instances_to_create.append(obj)
                existing_measurements.append((dt, values[0], values[1], values[2], sensor_id))
                print('others created')

        Measurement.objects.bulk_create(instances_to_create, batch_size=2000)
        MeteoData.objects.bulk_create(meteo_instances_to_create, batch_size=2000)
