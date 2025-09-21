import json

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import redirect

from reports.services.download_excel_report import DownloadExcelReport
from webhook.models import Sensor, Measurement


@login_required(login_url='authorization:login')
def get_sensors(request):
    location = request.GET.get('location')
    sensors = Sensor.objects.filter(location=location).values('name', 'id')
    return JsonResponse(list(sensors), safe=False)


@login_required(login_url='authorization:login')
def menu(request):
    return redirect('monitoring:index')


@login_required(login_url='authorization:login')
def download_excel_report(request):
    data = json.loads(request.body)
    return DownloadExcelReport(data).download_excel_report()


@login_required(login_url='authorization:login')
def update_measurements(request):
    data = json.loads(request.body)
    if request.method == 'POST':
        try:
            sensor = Sensor.objects.get(id=data.get('sensor_id'))
        except Sensor.DoesNotExist:
            return JsonResponse({'status': 'error'})
        measurement_types = sensor.supported_types.all()

        date = data.get('date')
        for type in measurement_types:
            value = data.get(type.code)
            obj_id = data.get(f"{type.code}_id")

            measurement = Measurement.objects.get(id=obj_id)
            measurement.value = float(value.replace(',', '.'))
            measurement.date = date
            measurement.save()

        return JsonResponse({'status': 'ok'})
    return JsonResponse({'status': 'error'})


@login_required(login_url='authorization:login')
def delete_measurements(request):
    data = json.loads(request.body)
    if request.method == 'POST':
        for type, id in data.items():
            if Measurement.objects.filter(id=id).exists():
                instance = Measurement.objects.get(id=id)
                instance.delete()
        return JsonResponse({'status': 'ok'})
    return JsonResponse({'status': 'error'})
