import json
import pandas

from datetime import datetime, timedelta

from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.utils import timezone

from core import extra_functions
from sensors.models import ManualData, InstanceManualData
from webhook.sensor_parsing import sensor_types as sensor_types_dict
from webhook.models import Measurement, ExampleMeasurement, Sensor
from monitoring.services.index import LatestData
from monitoring.services.export_to_excel import ExportToExcel

def can_add_threshold(user):
    return user.can_add_threshold or user.is_superuser


@login_required(login_url='authorization:login')
def index(request):
    context = LatestData().get_data()

    for sensor_id, values in context['latest_values'].items():
        cnt = 1 if values['value1'] == '#NV' else 0
        cnt = cnt+1 if values['value2'] == '#NV' else cnt
        cnt = cnt+1 if values['value3'] == '#NV' else cnt
        sensor_types = sensor_types_dict[values['sensor_type']]
        cnt -= (3-len(sensor_types))
        if len(sensor_types) == 1 and cnt > 0:
            context['latest_values'][sensor_id]['status'] = 'Нет данных'
        elif len(sensor_types) == 2:
            if cnt == 1:
                context['latest_values'][sensor_id]['status'] = 'Тревога'
            if cnt == 2:
                context['latest_values'][sensor_id]['status'] = 'Нет данных'
        elif len(sensor_types) == 3:
            if cnt == 1:
                context['latest_values'][sensor_id]['status'] = 'Предупреждение'
            elif cnt == 2:
                context['latest_values'][sensor_id]['status'] = 'Тревога'
            elif cnt == 3:
                context['latest_values'][sensor_id]['status'] = 'Нет данных'

    return render(request, 'monitoring/index.html', context)


def fire_signal(request):
    instance = Measurement.objects.get(id=6501)
    new_instance = ExampleMeasurement(
        date=instance.date,
        sensor_id=instance.sensor_id,
        value1=instance.value1,
        value2=instance.value2,
        value3=instance.value3,
    )
    new_instance.save()
    return redirect('monitoring:index')


def format_date(date):
    res = pandas.to_datetime(date).to_pydatetime()
    return timezone.make_aware(res)


def add_data_manually(request):
    if request.method == 'POST':
        date = format_date(request.POST.get('date'))
        sensor_id = request.POST.get('sensor_id')
        type_id = request.POST.get('type_id')
        value = request.POST.get('value')
        try:
            instance = Measurement(date=date, sensor_id=sensor_id, type_id=type_id, value=value)
            instance.save()
            print('saved')
            return redirect('monitoring:add-data-manually')
        except Exception as e:
            print(e)
            messages.error(request, 'Ошибка при сохранении')

    return render(request, 'monitoring/add_data_manually.html')


@login_required(login_url='authorization:login')
def settings_view(request):
    return render(request, 'monitoring/mysettings.html')


def export_to_excel(request):
    return ExportToExcel().export(request)


def add_data(request):
    latest_local_meteo = LatestData().get_latest_local_meteo_data()
    numbers = [n for n in range(1, 11)]

    if request.method == 'POST':
        location = request.POST.get('location')
        spot = request.POST.get('spot')
        button_action = request.POST.get('button_action')
        wind_speed_in_room = request.POST.get('wind_speed_in_room')

        if button_action == 'save':
            manual_data = ManualData(
                location=location,
                spot=spot,
                local_temperature=latest_local_meteo['temperature'],
                wind_speed_in_room = wind_speed_in_room,
                user=request.user,
            )
            manual_data.save()

            instances_to_create = []
            for i in range(1, 10):
                temperature = request.POST.get(f't{i}') or None
                humidity = request.POST.get(f'h{i}') or None
                img = request.FILES.get(f'img{i}')

                check = extra_functions.is_image(img)
                if img and not isinstance(check, bool):
                    messages.error(request, 'Неправильный формат или размер фото')
                    return redirect('monitoring:add-data')
                instance = InstanceManualData(
                    temperature=temperature,
                    humidity=humidity,
                    img=img,
                    number=str(i),
                    manual_data=manual_data,
                )
                instances_to_create.append(instance)
            InstanceManualData.objects.bulk_create(instances_to_create)
    return render(request, 'monitoring/add_data.html', {'latest_local_meteo': latest_local_meteo, 'numbers': numbers})


def data_list(request):
    return render(request, 'monitoring/data_list.html')