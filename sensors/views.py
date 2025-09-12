import time

from django.contrib import messages
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render, redirect

from sensors.models import SensorSettings
from webhook.models import Sensor
from webhook.sensor_parsing import sensor_types


# Create your views here.

def add_settings(request):
    return render(request, 'sensors/add_settings.html')


def add_dev_settings(request):
    sensors = Sensor.objects.all().order_by('location', 'name')
    if request.method == 'POST':
        submit_action = request.POST.get('submit_action')
        sensor_id = request.POST.get('sensor_id')
        type_name = request.POST.get('type_name')
        from_value = request.POST.get('from').replace(',', '.')
        to_value = request.POST.get('to').replace(',', '.')
        action = request.POST.get('action')
        status = request.POST.get('status')

        if submit_action == 'update':
            setting_id = request.POST.get('setting_id')
            instance = SensorSettings.objects.get(id=setting_id)
            instance.from_value = from_value
            instance.to_value = to_value
            instance.action = action
            instance.status = status
        else:
            instance = SensorSettings(
                sensor_id=sensor_id,
                type_name=type_name,
                from_value=from_value,
                to_value=to_value,
                action=action,
                status=status,
                user=request.user,
            )

        try:
            instance.save()
        except SensorSettings.DoesNotExist:
            messages.error(request, 'Настройка не найдена')
        except Exception as e:
            messages.error(request, 'Неправильные значения введены')
        return redirect(request.META.get('HTTP_REFERER', 'sensors:add_dev_settings'))

    data = {}
    for sensor in sensors:
        data[sensor.id] = {
            'name': sensor.name,
            'location': sensor.location,
            'spot': sensor.spot,
            'sensor_type': sensor.sensor_type,
            'image': sensor.image,
        }
        types = sensor_types[sensor.sensor_type]
        for i in range(1, len(types) + 1):
            existing_settings = SensorSettings.objects.filter(sensor_id=sensor.id, type_name=types[i - 1][0]).values(
                'id', 'from_value', 'to_value', 'action', 'status'
            )
            data[sensor.id][f'type{i}'] = {
                'name': types[i - 1][0],
                'sign': types[i - 1][1],
                'existing_settings': existing_settings,
            }

    paginator = Paginator(list(data.items()), 20)
    page = request.GET.get('page')
    paged_data = paginator.get_page(page)

    request_copy = request.GET.copy()
    if 'page' in request_copy:
        del request_copy['page']

    return render(request, 'sensors/add_dev_settings.html',
                  {
                      'sensors': paged_data,
                      'url': request_copy.urlencode()
                  })


def upload_sensor_image(request, sensor_id):
    if request.method == 'POST':
        uploaded_file = request.FILES.get('image')
        if not uploaded_file:
            return JsonResponse({'status': 'error', 'message': 'No file provided'}, status=400)

        if not uploaded_file.content_type.startswith('image/'):
            return JsonResponse({'status': 'error', 'message': 'Only image files allowed'}, status=400)

        # ✅ Optionally check file size (example: max 10MB)
        if uploaded_file.size > 10 * 1024 * 1024:
            return JsonResponse({'status': 'error', 'message': 'File too large'}, status=400)

        sensor = Sensor.objects.get(id=sensor_id)
        if sensor.image:
            sensor.image.delete(save=False)
        sensor.image = uploaded_file
        sensor.save()

        return JsonResponse({'status': 'success', 'image_url': sensor.image.url})

    return JsonResponse({'status': 'error', 'message': 'Invalid method'}, status=405)


def delete_setting(request):
    if request.method == 'POST':
        setting_id = request.POST.get('setting_id')
        try:
            SensorSettings.objects.get(id=setting_id).delete()
            return JsonResponse({'status': 'success'})
        except SensorSettings.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Settings not found'}, status=404)
    return JsonResponse({'status': 'error', 'message': 'Invalid method'}, status=405)
