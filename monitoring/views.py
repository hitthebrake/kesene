from http.client import responses

from django.contrib import messages
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.conf import settings
from django.db import connection
import json
import pandas
from django.utils import timezone


from webhook.models import Sensor, Measurement, MeteoData

import time
import requests

def can_add_threshold(user):
    return user.can_add_threshold or user.is_superuser





@login_required(login_url='authorization:login')
def table(request):
    data = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat=43.2975&lon=68.2708&appid={settings.WEATHER_API_KEY}&lang=ru')
    locations = set(sensor.location for sensor in Sensor.objects.all())
    return redirect()
    return render(request, 'monitoring/monitoring.html', {'locations': locations})


@login_required(login_url='authorization:login')
def index(request):
    data = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?lat=43.2975&lon=68.2708&appid={settings.WEATHER_API_KEY}&lang=ru'
    )
    print(data.json())
    return render(request, 'monitoring/index.html')


def check_limits(a, b, c, d):
    if a >= b or c >= d:
        return False, 'Неправильные лимиты'
    if b <= c or d <= a:
        return True, ''
    return False, 'Пересечение другими лимитами'





@login_required(login_url='authorization:login')
def get_types(request):
    sensor_id = request.GET.get('sensor_id')
    sensor = Sensor.objects.get(id=sensor_id)
    types = sensor.supported_types.values('id', 'label', 'code')
    return JsonResponse(list(types), safe=False)


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




