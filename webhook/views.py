import json

from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt

from webhook.models import WebhookRequest, Sensor, Measurement, MeteoData, ExampleWebhookRequest
from webhook.sensor_parsing import get_sensor_info, parse_dt, safe_float


@csrf_exempt
def webhook(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body.decode("utf-8"))

            WebhookRequest.objects.create(
                data=data,
            )

            return JsonResponse({"status": "success"})
        except json.JSONDecodeError:
            return HttpResponseBadRequest("Invalid JSON")

    return HttpResponseBadRequest("Only POST with JSON is allowed")


def copy_all_data(request):
    objects = WebhookRequest.objects.all()
    existing_sensors = {
        (name, location, spot, sensor_type): sid
        for name, location, spot, sensor_type, sid in Sensor.objects.values_list(
            'name', 'location', 'spot', 'sensor_type', 'id'
        )
    }
    existing_measurements = set(
        (date, safe_float(v1), safe_float(v2), safe_float(v3), sensor)
        for date, v1, v2, v3, sensor in Measurement.objects
        .values_list('date', 'value1', 'value2', 'value3', 'sensor_id')
    )
    existing_meteo_data = set(
        (date, safe_float(v1), safe_float(v2), safe_float(v3), safe_float(v4), safe_float(v5),
         safe_float(v6), safe_float(v7))
        for date, v1, v2, v3, v4, v5, v6, v7 in MeteoData.objects.values_list(
            'date', 'temperature', 'dewpoint', 'pressure', 'humidity', 'wind_speed',
            'wind_direction', 'precipitation')
    )

    instances_to_create = []
    meteo_instances_to_create = []

    for instance in objects:
        sheets = instance.data['sheets']

        for key, value in sheets.items():
            sensor_data = get_sensor_info(key)
            if len(sensor_data) == 0:
                continue

            # handling Meteo data
            if sensor_data['name']=='Метео данные':
                value[0] = parse_dt(value[0])
                for i in range(1, len(value)):
                    value[i] = 100000 if value[i] == "#NV" else float(value[i])
                    if value[i] > 10000 or value[i] < -10000:
                        value[i] = None

                date, temperature, dewpoint, pressure, humidity, wind_speed, wind_direction, precipitation = value
                if (date, temperature, dewpoint, pressure, humidity, wind_speed, wind_direction, precipitation) not in existing_meteo_data:
                    obj = MeteoData(
                        date=str(date),
                        temperature=temperature,
                        dewpoint=dewpoint,
                        pressure=pressure,
                        humidity=humidity,
                        wind_speed=wind_speed,
                        wind_direction=wind_direction,
                        precipitation=precipitation,
                    )
                    meteo_instances_to_create.append(obj)
                    print('repeatAAA')
                    existing_meteo_data.add((date, temperature, dewpoint, pressure, humidity, wind_speed, wind_direction, precipitation))
                else:
                    print("DONOt not not")
                continue

            # creates sensor
            key_tuple = (sensor_data['name'], sensor_data['location'], sensor_data['spot'], sensor_data['type'])
            sensor_id = existing_sensors.get(key_tuple)
            if not sensor_id:
                sensor = Sensor.objects.create(
                    name=sensor_data['name'],
                    location=sensor_data['location'],
                    spot=sensor_data['spot'],
                    sensor_type=sensor_data['type'],
                )
                existing_sensors[key_tuple] = sensor.id
                sensor_id = sensor.id

            date, *measurement_values = value
            dt = parse_dt(date)
            values = [100000, 100000, 100000]

            for i in range(len(measurement_values)):
                values[i] = 100000 if measurement_values[i] == "#NV" else float(measurement_values[i])
            for i in range(3):
                if values[i] > 10000 or values[i] < -10000:
                    values[i] = None


            # create measurement if it does not exist
            if not (dt, values[0], values[1], values[2], sensor_id) in existing_measurements:
                obj = Measurement(
                    date=str(dt), value1=values[0], value2=values[1], value3=values[2], sensor_id=sensor_id,
                )
                instances_to_create.append(obj)
                existing_measurements.add((dt, values[0], values[1], values[2], sensor_id))
                print('RepeatBBB')
            else:
                print("DONOt")

    Measurement.objects.bulk_create(instances_to_create, batch_size=2000)
    MeteoData.objects.bulk_create(meteo_instances_to_create, batch_size=2000)
    return redirect('monitoring:index')


def fire_signal(request):
    obj = WebhookRequest.objects.get(id=33300)
    instance = ExampleWebhookRequest(data=obj.data)
    instance.save()
    return redirect('monitoring:index')
