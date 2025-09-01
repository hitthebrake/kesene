import pandas

from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.utils import timezone

from webhook.models import Measurement, ExampleMeasurement
from monitoring.services.index import LatestData

def can_add_threshold(user):
    return user.can_add_threshold or user.is_superuser


@login_required(login_url='authorization:login')
def index(request):
    context = LatestData().get_data()
    return render(request, 'monitoring/index.html', context)


def fire_signal(request):
    instance = Measurement.objects.get(id=6001)
    new_instance = ExampleMeasurement(
        date=instance.date,
        sensor_id=instance.sensor_id,
        value1=instance.value1,
        value2=instance.value2,
        value3=instance.value3,
    )
    new_instance.save()
    return redirect('monitoring:index')


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
