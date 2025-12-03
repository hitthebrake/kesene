from django.http import JsonResponse
from django.shortcuts import render, redirect

from analytics.services.analytics import GetAnalytics
from analytics.services.export_to_excel import ExportAnalytics
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

def export_analytics(request):
    return ExportAnalytics(request).export()
