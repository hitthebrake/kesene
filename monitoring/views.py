from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.db import connection

from reports.models import Sensor, Measurement, MeasurementType

import time
import requests

@login_required(login_url='authorization:login')
def table(request):
    data = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat=43.2975&lon=68.2708&appid={settings.WEATHER_API_KEY}&lang=ru')
    locations = set(sensor.location for sensor in Sensor.objects.all())


    return render(request, 'monitoring/monitoring.html', {'locations': locations})


@login_required(login_url='authorization:login')
def index(request):
    overall_start = time.time()
    sensors = Sensor.objects.prefetch_related('supported_types')

    start = time.time()
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT DISTINCT ON (sensor_id, type_id)
                   sensor_id, type_id, value
            FROM reports_measurement
            ORDER BY sensor_id, type_id, date DESC
        """)
        raw_rows = cursor.fetchall()
    latest_values = {(s_id, t_id): value for s_id, t_id, value in raw_rows}
    end = time.time()
    print('SQL duration:', end - start)

    # Build values
    values = []
    for sensor in sensors:
        data = {'name': sensor.name, 'location': sensor.location, 'sensor_id': sensor.id, 'data': []}
        for t in sensor.supported_types.all():
            data['data'].append({
                'value': latest_values.get((sensor.id, t.id)),
                'id': t.id,
                'label': t.label,
                'code': t.code,
            })
        values.append(data)

    overall_end = time.time()
    print('Overall duration:', overall_end - overall_start)

    return render(request, 'monitoring/monitoring.html', {
        'values': values,
    })
