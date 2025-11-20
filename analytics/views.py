from django.http import JsonResponse
from django.shortcuts import render

from webhook.models import Sensor


# Create your views here.
def analytics(request):
    return render(request, 'analytics/analytics.html')


def get_location_info(request, location: str):
    sensors = Sensor.objects.filter(location=location)
    types = []
    for sensor in sensors:
        if sensor.sensor_type not in types:
            types.append(sensor.sensor_type)
    return JsonResponse({'types': types})