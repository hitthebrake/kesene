import json, pandas

from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.utils import timezone
from django.contrib import messages
from django.core.serializers.json import DjangoJSONEncoder
from django.utils.safestring import mark_safe
from django.utils.dateparse import parse_date, parse_time
from datetime import datetime


from urllib.parse import urlencode

from pip._internal import locations

from .models import MeasurementType, Measurement, Sensor, Threshold
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

    thresholds = Threshold.objects.filter(sensor__in=sensors)
    thresholds_json = [
        {"type": t.type.code, "limit1": t.limit1, "limit2": t.limit2}
        for t in thresholds
    ]

    url = urlencode(request.GET)
    if 'page' in request.GET:
        copy_request = request.GET.copy()
        del copy_request['page']
        url = urlencode(copy_request)

    paginator = Paginator(measurements, 200)
    page = request.GET.get('page') or 1
    paged_measurements = paginator.get_page(page)

    context = {
        'thresholds': thresholds,
        'paged_measurements': paged_measurements,
        'sensors': sensors,
        'measurement_types': types,
        'url': url,
        "thresholds_json": mark_safe(json.dumps(thresholds_json, cls=DjangoJSONEncoder)),
        "measurement_types_json": mark_safe(json.dumps(list(types.values('code')), cls=DjangoJSONEncoder)),
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
def thresholds(request):
    locations = set(sensor.location for sensor in Sensor.objects.all())
    if request.method == 'POST':
        sensor_id = request.POST.get('sensor_id')
        if Sensor.objects.filter(id=sensor_id).exists():
            sensor = Sensor.objects.get(id=sensor_id)
            types = sensor.supported_types.all()
            for type in types:
                limit1 = request.POST.get(f'{type.code}_first')
                limit2 = request.POST.get(f'{type.code}_second')

                if Threshold.objects.filter(sensor=sensor, type=type).exists():
                    print(f'{type.label} threshold already exists')
                else:
                    instance = Threshold(sensor=sensor, type=type, limit1=limit1, limit2=limit2)
                    instance.save()

    return render(request, 'reports/thresholds.html', {'locations': locations})

def get_threshold_types(request):
    sensor = Sensor.objects.get(id=request.GET.get('sensor_id'))
    if sensor is None:
        return JsonResponse({'status': 'error', 'error': 'Датчик не найден в базе данных'})
    types = sensor.supported_types.all().values('id', 'code', 'label')
    return JsonResponse(list(types), safe=False)


@login_required(login_url='authorization:login')
def download_excel_report(request):
    pass



