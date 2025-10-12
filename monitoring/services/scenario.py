
from django.utils import timezone
from sensors.models import LocationScenario, SensorScenario, ScenarioInstance


def get_season():
    month = timezone.now().month
    months = [12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    idx = months.index(month)
    return idx // 3 + 1


class ScenarioCheck:
    @staticmethod
    def scenario_check_by_meteo_data(scenarios, meteo_data):
        # meteo_data = LatestData().get_latest_local_meteo_data()
        valid_scenarios = []
        for scenario in scenarios:
            if scenario.from_temperature <= meteo_data["temperature"] <= scenario.to_temperature and \
                    scenario.from_humidity <= meteo_data["humidity"] <= scenario.to_humidity and \
                    scenario.from_dewpoint <= meteo_data["dewpoint"] <= scenario.to_dewpoint and \
                    scenario.from_pressure <= meteo_data["pressure"] <= scenario.to_pressure and \
                    scenario.from_wind_speed <= meteo_data["wind_speed"] <= scenario.to_wind_speed and \
                    scenario.from_wind_direction <= meteo_data["wind_direction"] <= scenario.to_wind_direction and \
                    scenario.from_precipitation <= meteo_data["precipitation"] <= scenario.to_precipitation:
                valid_scenarios.append(scenario)
        return valid_scenarios

    @staticmethod
    def scenario_check_by_sensors(scenarios, latest_data):
        # latest_data = LatestData().get_latest_measurements()
        valid_scenarios = []
        for scenario in scenarios:
            flag = True
            sensor_scenarios = SensorScenario.objects.filter(scenario=scenario).prefetch_related('sensor')
            for sensor_scenario in sensor_scenarios:
                sensor_id = sensor_scenario.sensor.id
                data = latest_data.get(sensor_id)
                if data:
                    if (data['value1'] == "#NV" or sensor_scenario.from1 <= data['value1'] <= sensor_scenario.to1) and \
                            (data['value2'] == "#NV" or sensor_scenario.from2 <= data['value2'] <= sensor_scenario.to2) and \
                            (data['value3'] == "#NV" or sensor_scenario.from3 <= data['value3'] <= sensor_scenario.to3):
                        continue
                    else:
                        flag = False
                        break
            if flag:
                valid_scenarios.append(scenario)

        return valid_scenarios


    def scenario_check(self, latest_data, meteo_data):
        scenarios = LocationScenario.objects.filter(season=get_season()).prefetch_related('user')
        scenarios = self.scenario_check_by_meteo_data(scenarios, meteo_data)
        scenarios = self.scenario_check_by_sensors(scenarios, latest_data)

        active_scenarios = ScenarioInstance.objects.filter(
            scenario__in=scenarios, status__in=['pending', 'in_progress']
        ).values_list('scenario__id', flat=True)

        all_active_scenarios = ScenarioInstance.objects.filter(status__in=['pending', 'in_progress'])
        for scenario in all_active_scenarios:
            if scenario.id not in active_scenarios:
                scenario.resolve()


        for scenario in scenarios:
            if scenario.id not in active_scenarios:
                scenario_instance = ScenarioInstance(scenario=scenario)
                scenario_instance.save()

        active_scenarios = ScenarioInstance.objects.filter(
            scenario__in=scenarios, status__in=['pending', 'in_progress']
        ).select_related('scenario', 'user')

        return active_scenarios


