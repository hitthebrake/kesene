import json, pandas

from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.paginator import Paginator
from django.utils import timezone
from django.contrib import messages
from django.utils.dateparse import parse_date, parse_time

from datetime import datetime, timedelta

from .models import MeasurementType, Measurement, Sensor
# Create your views here.

def format_date(date):
    res = pandas.to_datetime(date).to_pydatetime()
    return timezone.make_aware(res)

@login_required(login_url='authorization:login')
def get_sensors(request):
    location = request.GET.get('location')
    sensors = Sensor.objects.filter(location=location).values('name', 'id')
    return JsonResponse(list(sensors), safe=False)


@login_required(login_url='authorization:login')
def menu(request):
    return render(request, 'reports/menu.html')


def calculate_stat(sensor, type, data, duration):
    total_val, count_none, count_tot = 0, 0, 0
    maximum, minimum = -100000, 100000

    for obj in data:
        if obj['sensor'] == sensor.id and obj['type'] == type.id:
            if obj['value'] is None or obj['value']=="":
                count_none += 1
            else:
                count_tot += 1
                total_val += obj['value']
                maximum = max(maximum, obj['value'])
                minimum = min(minimum, obj['value'])

    average = None
    if count_tot > 0:
        average = round(total_val / count_tot, 3)

    interval = 10 if 'ТвОВв' in str(sensor.name) else 2
    time_active = timedelta(minutes=count_tot * interval)

    result = {'average': average, 'max': maximum, 'min': minimum,
              'active_duration': time_active, 'passive_duration': duration - time_active,
              'total_count': count_tot, 'interval': interval,
              }
    return result


def get_url(request):
    if 'page' in request:
        del request['page']
    return request.urlencode()


@login_required(login_url='authorization:login')
def report_details(request):
    date_start = parse_date(request.GET.get('date_s'))
    date_end = parse_date(request.GET.get('date_e'))
    time_start = parse_time(request.GET.get('time_s'))
    time_end = parse_time(request.GET.get('time_e'))

    start = format_date(datetime.combine(date_start, time_start))
    end = format_date(datetime.combine(date_end, time_end))

    sensor_ids = request.GET.getlist('sensor_id')
    sensors = Sensor.objects.filter(id__in=sensor_ids)
    types = MeasurementType.objects.filter(sensor__in=sensors).values('id', 'label', 'code').distinct()

    data = Measurement.objects.filter(date__range=(start, end), sensor__in=sensors).order_by('date').values('date', 'value', 'type', 'sensor', 'id')

    statistics = {}
    for sensor in sensors:
        statistics[f'{sensor.location}: {sensor.name}'] = {}
        for type in sensor.supported_types.all():
            statistics[f'{sensor.location}: {sensor.name}'][type.label] = calculate_stat(sensor, type, data, end-start)



    measurements = {}
    for d in data:
        if (d['date'], d['sensor']) not in measurements:
            measurements[(d['date'], d['sensor'])] = []
        measurements[(d['date'], d['sensor'])].append(d)

    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'filter':
            type = request.POST.get('filter')
            order = (request.POST.get('order') == 'desc')
            for m in types:
                if m["id"] == type:
                    type = m

            sorting_key = (lambda x: next(((y['value'] or 0) for y in x[1] if y.type == type), 0)) if type in types else lambda x: x[0]
            measurements = sorted(list(measurements.items()), key=sorting_key, reverse=order)
        elif action == 'create':
            sensor_id = request.POST.get('sensor_id')

            if Sensor.objects.filter(id=sensor_id).exists():
                sensor = Sensor.objects.get(id=sensor_id)
                measurement_types = sensor.supported_types.all()
                date = request.POST.get('date')

                if Measurement.objects.filter(date=format_date(date), sensor=sensor).exists():
                    messages.error(request, 'Данные уже существуют')
                else:
                    for type in measurement_types:
                        value = float(request.POST.get(f'{type.code}').replace(',', '.'))
                        instance = Measurement(date=format_date(date), sensor=sensor, type=type, value=value)
                        instance.save()

    if not isinstance(measurements, list):
        measurements = list(measurements.items())


    paginator = Paginator(measurements, 200)
    page = request.GET.get('page')
    paged_measurements = paginator.get_page(page)

    context = {
        'start': start,
        'end': end,
        'paged_measurements': paged_measurements,
        'sensors': sensors,
        'measurement_types': types,
        'url': get_url(request.GET.copy()),
        'statistics': statistics,
    }

    return render(request, 'reports/report_details.html', context)

@login_required(login_url='authorization:login')
def update_measurements(request):
    data = json.loads(request.body)
    if request.method == 'POST':
        try:
            sensor = Sensor.objects.get(id=data.get('sensor_id'))
        except Sensor.DoesNotExist:
            return JsonResponse({'status': 'error'})
        measurement_types = sensor.supported_types.all()

        date = data.get('date')
        for type in measurement_types:
            value = data.get(type.code)
            obj_id = data.get(f"{type.code}_id")

            measurement = Measurement.objects.get(id=obj_id)
            measurement.value = float(value.replace(',', '.'))
            measurement.date = date
            measurement.save()

        return JsonResponse({'status': 'ok'})
    return JsonResponse({'status': 'error'})


@login_required(login_url='authorization:login')
def delete_measurements(request):
    data = json.loads(request.body)
    if request.method == 'POST':
        for type, id in data.items():
            if Measurement.objects.filter(id=id).exists():
                instance = Measurement.objects.get(id=id)
                instance.delete()
        return JsonResponse({'status': 'ok'})
    return JsonResponse({'status': 'error'})


@login_required(login_url='authorization:login')
def download_excel_report(request):
    pass



