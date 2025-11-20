from django.http import JsonResponse
from django.shortcuts import render

from analytics.services.analytics import GetAnalytics
from webhook.models import Sensor


# Create your views here.
def analytics(request):
    context = GetAnalytics(request).analytics()
    return render(request, 'analytics/analytics.html', context)

def get_location_info(request, location: str):
    if location=='all':
        sensors = Sensor.objects.all()
    else:
        sensors = Sensor.objects.filter(location=location)
    types = list(sensors.values_list('sensor_type', flat=True).distinct())
    return JsonResponse({'types': types})
