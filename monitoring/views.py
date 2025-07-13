from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings

from reports.models import Sensor, Measurement, MeasurementType

import requests
@login_required(login_url='authorization:login')
def table(request):
    data = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat=43.2975&lon=68.2708&appid={settings.WEATHER_API_KEY}&lang=ru')
    locations = set(sensor.location for sensor in Sensor.objects.all())


    return render(request, 'monitoring/monitoring.html', {'locations': locations})