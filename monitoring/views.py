from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.conf import settings
from django.db import connection
from django.db.models import OuterRef, Subquery, Prefetch

from reports.models import Sensor, Threshold, Measurement, MeasurementType

import time
import requests

def can_add_threshold(user):
    return user.can_add_threshold or user.is_superuser


@user_passes_test(can_add_threshold, login_url='authorization:login')
def delete_threshold(request):
    if request.method == 'POST':
        id = request.POST.get('threshold_id')
        try:
            threshold = Threshold.objects.get(id=id)
            threshold.delete()
        except Threshold.DoesNotExist:
            pass
    return redirect('monitoring:thresholds')

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
                       SELECT s.sensor_id, s.type_id, m.value
                       FROM (SELECT DISTINCT sensor_id, type_id
                             FROM reports_measurement) AS s
                                CROSS JOIN LATERAL (
                           SELECT value
                           FROM reports_measurement m
                           WHERE m.sensor_id = s.sensor_id
                             AND m.type_id = s.type_id
                           ORDER BY m.date DESC
                           LIMIT 1
                           ) AS m;
                       """)
        raw_rows = cursor.fetchall()
    latest_values = {(s_id, t_id): value for s_id, t_id, value in raw_rows}
    end = time.time()
    print('SQL duration:', end - start)

    # Thresholds
    thresholds = Threshold.objects.select_related('sensor', 'type').values(
        'id', 'color',
        'sensor__id', 'type__id',
        'sensor__name', 'sensor__location',
        'type__label', 'type__code',
        'description', 'upper_limit', 'lower_limit'
    )

    # Build values
    values = []
    for sensor in sensors:
        data = {'name': sensor.name, 'location': sensor.location, 'sensor_id': sensor.id, 'data': []}
        for t in sensor.supported_types.all():
            value = latest_values.get((sensor.id, t.id))
            d = {
                'value': value,
                'id': t.id,
                'label': t.label,
                'code': t.code,
                'color' : '#32CD32',
                'description': 'Все нормально!',
            }

            for threshold in thresholds:
                if threshold['sensor__id'] == sensor.id and threshold['type__id'] == t.id:
                    if threshold['upper_limit'] >= value >= threshold['lower_limit']:
                        d['color'] = threshold['color']
                        d['description'] = threshold['description']


            data['data'].append(d)
        values.append(data)

    overall_end = time.time()
    print('Overall duration:', overall_end - overall_start)

    return render(request, 'monitoring/monitoring.html', {
        'values': values,
    })

def check_limits(a, b, c, d):
    if a >= b or c >= d:
        return False, 'Неправильные лимиты'
    if b <= c or d <= a:
        return True, ''
    return False, 'Пересечение другими лимитами'

@user_passes_test(can_add_threshold, login_url='authorization:login')
def thresholds_view(request):
    thresholds = Threshold.objects.select_related('sensor', 'type').values(
        'id', 'color',
        'sensor__id', 'type__id',
        'sensor__name', 'sensor__location',
        'type__label', 'type__code',
        'description', 'upper_limit', 'lower_limit'
    )

    if request.method == 'POST':
        sensor_id = int(request.POST.get('sensor_id'))
        type_id = int(request.POST.get('type_id'))
        color_code = request.POST.get('color_code')
        lower_limit = float(request.POST.get('lower_limit').replace(',', '.'))
        upper_limit = float(request.POST.get('upper_limit').replace(',', '.'))
        description = request.POST.get('description')

        for threshold in thresholds:
            if threshold['sensor__id'] == sensor_id and threshold['type__id'] == type_id:
                check, message = check_limits(lower_limit, upper_limit, threshold['lower_limit'], threshold['upper_limit'])
                if not check:
                    messages.error(request, message)
                    return render(request, 'monitoring/thresholds_view.html', {'thresholds': thresholds})

        instance = Threshold(
            sensor_id=sensor_id,
            type_id=type_id,
            color=color_code,
            lower_limit=lower_limit,
            upper_limit=upper_limit,
            description=description
        )
        instance.save()
        return redirect('monitoring:thresholds')

    return render(request, 'monitoring/thresholds_view.html', {'thresholds': thresholds})

@login_required(login_url='authorization:login')
def get_types(request):
    sensor_id = request.GET.get('sensor_id')
    sensor = Sensor.objects.get(id=sensor_id)
    types = sensor.supported_types.values('id', 'label', 'code')
    return JsonResponse(list(types), safe=False)

