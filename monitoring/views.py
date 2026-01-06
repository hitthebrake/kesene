from datetime import date

from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.utils import timezone

from core import extra_functions
from monitoring.services.export_to_excel import ExportToExcel
from monitoring.services.index import LatestData
from monitoring.services.manual_data_export import ManualDataExport
from monitoring.telegram_bot import broadcast_form
from sensors.models import ManualData, InstanceManualData, ScenarioInstance
from webhook.models import Measurement, ExampleMeasurement
from webhook.sensor_parsing import get_sensor_types


@login_required(login_url="authorization:login")
def index(request):
    context = LatestData().get_data()
    for sensor_id, values in context['latest_values'].items():
        cnt = 1 if values['value1'] == '#NV' else 0
        cnt = cnt + 1 if values['value2'] == '#NV' else cnt
        cnt = cnt + 1 if values['value3'] == '#NV' else cnt
        sensor_types = get_sensor_types(values['sensor_type'])
        cnt -= (3 - len(sensor_types))
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


@login_required(login_url="authorization:login")
def settings_view(request):
    return render(request, 'monitoring/mysettings.html')


@login_required(login_url="authorization:login")
def export_to_excel(request):
    return ExportToExcel().export(request)


def map_data(data):
    result = {}
    if data:
        instances = InstanceManualData.objects.filter(manual_data=data)
        for instance in instances:
            result[instance.number] = {
                'id': instance.id,
                'temperature': instance.temperature,
                'humidity': instance.humidity,
                'img': instance.img.url if instance.img else None,
            }

        result['wind_speed'] = data.wind_speed_in_room
    return result


@user_passes_test(extra_functions.can_add_data, login_url="authorization:login")
def add_data(request):
    latest_local_meteo = LatestData().get_latest_local_meteo_data()
    numbers = [n for n in range(1, 11)]

    if request.method == 'POST':
        location = request.POST.get('location')
        spot = request.POST.get('spot')
        draft = ManualData.objects.filter(location=location, spot=spot, is_draft=True).first()
        manual_data = ManualData(location=location, spot=spot)
        existing_instances = []
        if draft:
            if draft.created_date != date.today():
                draft.is_draft = False
                draft.save()
            else:
                manual_data = draft
                existing_instances = InstanceManualData.objects.filter(manual_data=manual_data)

        button_action = request.POST.get('button_action')
        wind_speed_in_room = request.POST.get('wind_speed_in_room')

        manual_data.wind_speed_in_room = wind_speed_in_room.replace(',', '.') if wind_speed_in_room else None
        manual_data.local_temperature = latest_local_meteo['temperature']
        manual_data.user = request.user

        if button_action == 'draft':
            manual_data.is_draft = True
        else:
            manual_data.is_draft = False

        manual_data.save()
        instances_to_create = []
        instances_to_update = []

        for i in range(1, 11):
            temperature = request.POST.get(f't{i}').replace(',', '.') if request.POST.get(f't{i}') else None
            humidity = request.POST.get(f'h{i}').replace(',', '.') if request.POST.get(f'h{i}') else None
            img = request.FILES.get(f'img{i}')
            check = extra_functions.is_image(img)
            if img and not isinstance(check, bool):
                messages.error(request, 'Неправильный формат или размер фото')
                return redirect('monitoring:add-data')
            if not (temperature or humidity or img):
                continue
            if existing_instances and existing_instances.filter(number=str(i)).exists():
                obj = existing_instances.filter(number=str(i)).first()
                obj.temperature = temperature if not obj.temperature else obj.temperature
                obj.humidity = humidity if not obj.humidity else obj.humidity
                obj.img = img if not obj.img else obj.img
                if img:
                    obj.save()
                else:
                    instances_to_update.append(obj)
            else:
                instance = InstanceManualData(
                    temperature=temperature,
                    humidity=humidity,
                    img=img,
                    number=str(i),
                    manual_data=manual_data,
                )
                if img:
                    instance.save()
                else:
                    instances_to_create.append(instance)
        InstanceManualData.objects.bulk_create(instances_to_create)
        InstanceManualData.objects.bulk_update(instances_to_update, ['temperature', 'humidity', 'img'])

    instances = (
        InstanceManualData.objects
        .select_related('manual_data', 'manual_data__user')
        .filter(
            manual_data__is_draft=False,
            manual_data__created_date=timezone.now().date()
        )
        .order_by('created_time')[:10]
    )

    drafts = ManualData.objects.filter(is_draft=True).prefetch_related('instance')
    context = {
        'perimeter_south': map_data(drafts.filter(location='Периметр', spot='Юг').first()),
        'perimeter_north': map_data(drafts.filter(location='Периметр', spot='Север').first()),
        'perimeter_west': map_data(drafts.filter(location='Периметр', spot='Запад').first()),
        'perimeter_east': map_data(drafts.filter(location='Периметр', spot='Восток').first()),
        'roof_south': map_data(drafts.filter(location='Кровля', spot='Юг').first()),
        'roof_north': map_data(drafts.filter(location='Кровля', spot='Север').first()),
        'roof_west': map_data(drafts.filter(location='Кровля', spot='Запад').first()),
        'roof_east': map_data(drafts.filter(location='Кровля', spot='Восток').first()),
        'latest_local_meteo': latest_local_meteo,
        'numbers': numbers,
        'last_instances': instances,
    }
    return render(request, 'monitoring/add_data.html', context)


@login_required(login_url="authorization:login")
def data_list(request):
    instances = InstanceManualData.objects.select_related('manual_data', 'manual_data__user') \
        .filter(manual_data__is_draft=False).order_by('manual_data__created_date', 'created_time')
    location = request.GET.get('location', "")
    spot = request.GET.get('spot', "")

    if location and spot:
        if location == 'Помещения':
            instances = instances.filter(manual_data__location=spot)
        elif location == 'Периметр' or location == 'Кровля':
            instances = instances.filter(manual_data__location=location, manual_data__spot=spot)

    paginator = Paginator(instances, 20)
    page = request.GET.get('page')
    instances = paginator.get_page(page)

    request_copy = request.GET.copy()
    if 'page' in request_copy:
        del request_copy['page']

    context = {
        'location': location,
        'spot': spot,
        'url': request_copy.urlencode(),
        'instances': instances
    }
    return render(request, 'monitoring/data_list.html', context)


@login_required(login_url="authorization:login")
def manual_data_export(request):
    return ManualDataExport().export(request)

@login_required(login_url="authorization:login")
def get_draft_data(request, location):
    if not location:
        return JsonResponse({'message': 'Локация не передана или не найдена'}, status=400)

    drafts = ManualData.objects.filter(is_draft=True, location=location).prefetch_related('instance').first()

    return JsonResponse(map_data(drafts))


@login_required(login_url="authorization:login")
def scenario_update(request, scenario_id, action):
    scenario = ScenarioInstance.objects.get(id=scenario_id)
    if action == 'pending':
        scenario.start_pending()
    elif action == 'in_progress':
        scenario.start_progress(request.user)
        broadcast_form(request, scenario_id)
    elif action == 'resolved':
        scenario.resolve()
    return redirect('monitoring:index')
