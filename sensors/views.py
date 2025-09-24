from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render, redirect

from core import extra_functions
from core.extra_functions import get_parameter_sign
from sensors.models import SensorSettings
from webhook.models import Sensor
from webhook.sensor_parsing import sensor_types
# Create your views here.


@user_passes_test(extra_functions.can_add_settings, login_url="authorization:login")
def add_settings(request):
    return render(request, 'sensors/add_settings.html')


def check_limits(from_value, to_value, sensor_id, type_name):
    sensor_settings = SensorSettings.objects.filter(sensor__id=sensor_id, type_name=type_name)

    if from_value is None and to_value is None:
        if sensor_settings.filter(from_value=from_value, to_value=to_value).exists():
            return "error", "Данные существуют !!!"
        return 'success', 'Данные сохранены'

    if from_value is None or to_value is None:
        return "error", "Оба значения должны быть одинакого типа !!!"

    try:
        f, t = float(from_value), float(to_value)
    except:
        return "error", "Введите число либо #NV !!!"

    if f >= t:
        return "error", "Первая значение должна быть меньше второго!!!"
    else:
        for obj in sensor_settings:
            if not (obj.from_value is None and obj.to_value is None):
                if float(obj.from_value) <= f < float(obj.to_value) or \
                        float(obj.from_value) < t <= float(obj.to_value):
                    return "error", f"Пересечение с диапазоном [{obj.from_value} - {obj.to_value}]"
    return 'success', 'Данные сохранены'


@user_passes_test(extra_functions.can_add_settings, login_url="authorization:login")
def add_dev_settings(request):
    sensors = Sensor.objects.all().order_by('location', 'name')

    if request.method == 'POST':
        submit_action = request.POST.get('submit_action')
        sensor_id = request.POST.get('sensor_id')
        type_name = request.POST.get('type_name')
        action = request.POST.get('action')
        status = request.POST.get('status')

        from_value = request.POST.get('from').replace(',', '.')
        to_value = request.POST.get('to').replace(',', '.')
        if from_value.lower() in "#nv":
            from_value = None
        if to_value.lower() in "#nv":
            to_value = None

        check_status, check_message = check_limits(from_value, to_value, sensor_id, type_name)
        if check_status == 'error':
            messages.error(request, check_message)
            return redirect(request.META.get('HTTP_REFERER', 'sensors:add_dev_settings'))

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
            messages.success(request, check_message)
        except SensorSettings.DoesNotExist:
            messages.error(request, 'Настройка не найдена')
        except Exception as e:
            print(e)
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


@login_required(login_url='authorization:login')
def dev_settings_list(request):
    sensor_settings = SensorSettings.objects.filter(is_active=True).select_related('sensor', 'user').order_by('-created_at')
    if request.GET.get('location'):
        location = request.GET.get('location')
        sensor_settings = sensor_settings.filter(sensor__location=location)

    parsed_settings = {}
    for setting in sensor_settings:
        parsed_settings[setting.id] = {
            'sensor_name': setting.sensor.name,
            'sensor_location': setting.sensor.location,
            'sensor_spot': setting.sensor.spot,
            'sensor_type': setting.sensor.sensor_type,
            'sensor_image': setting.sensor.image,

            'user_full_name': f'{setting.user.last_name} {setting.user.first_name} {setting.user.patronym}',
            'created_at': setting.created_at.strftime('%d.%m.%Y'),
            'status': setting.status,
            'action': setting.action,
            'parameter': setting.type_name,
            'parameter_sign': get_parameter_sign(setting.sensor.sensor_type, setting.type_name),
            'from_value': setting.from_value if setting.from_value else '#NV',
            'to_value': setting.to_value if setting.to_value else '#NV',
        }
        if parsed_settings[setting.id]['from_value'] == '#NV' or parsed_settings[setting.id]['to_value'] == '#NV':
            parsed_settings[setting.id]['parameter_sign'] = ''

    context = {
        'sensor_settings': parsed_settings,
    }
    return render(request, "sensors/dev_set_list.html", context)


@user_passes_test(extra_functions.can_add_settings, login_url="authorization:login")
def upload_sensor_image(request, sensor_id):
    if request.method == 'POST':
        uploaded_file = request.FILES.get('image')
        check = extra_functions.is_image(uploaded_file)
        if not isinstance(check, bool):
            return check

        sensor = Sensor.objects.get(id=sensor_id)
        if sensor.image:
            sensor.image.delete(save=False)
        sensor.image = uploaded_file
        sensor.save()

        return JsonResponse({'status': 'success', 'image_url': sensor.image.url})

    return JsonResponse({'status': 'error', 'message': 'Invalid method'}, status=405)


@user_passes_test(extra_functions.can_add_settings, login_url="authorization:login")
def delete_setting(request):
    if request.method == 'POST':
        setting_id = request.POST.get('setting_id')
        try:
            SensorSettings.objects.get(id=setting_id).delete()
            return JsonResponse({'status': 'success'})
        except SensorSettings.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Settings not found'}, status=404)
    return JsonResponse({'status': 'error', 'message': 'Invalid method'}, status=405)
