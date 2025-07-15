from reports.models import Sensor

def location_list(request):
    locations = Sensor.objects.values_list('location', flat=True).distinct()
    return {'location_list': locations}