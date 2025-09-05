from django.shortcuts import render, redirect

from sensors.models import SensorSettings
from webhook.models import Sensor
from webhook.sensor_parsing import sensor_types

# Create your views here.

def add_settings(request):
    return render(request, 'sensors/add_settings.html')


def add_dev_settings(request):
    sensors = Sensor.objects.all().order_by('location', 'name')
    data = {}
    if request.method == 'POST':
        sensor_id = request.POST.get('sensor_id')
        type_name = request.POST.get('type_name')
        from_value = request.POST.get('from')
        to_value = request.POST.get('to')
        action = request.POST.get('action')
        status = request.POST.get('status')

        instance = SensorSettings(
            sensor_id=sensor_id,
            type_name=type_name,
            from_value=from_value,
            to_value=to_value,
            action=action,
            status=status,
        )
        instance.save()

        return redirect('sensors:add_dev_settings')

    for sensor in sensors:
        data[sensor.id] = {
            'name': sensor.name,
            'location': sensor.location,
            'spot': sensor.spot,
            'sensor_type': sensor.sensor_type,
        }
        types = sensor_types[sensor.sensor_type]
        for i in range(1, len(types)+1):
            data[sensor.id][f'type{i}'] = {
                'name': types[i-1][0],
                'sign': types[i-1][1],
            }

    return render(request, 'sensors/add_dev_settings.html', {'sensors': data})