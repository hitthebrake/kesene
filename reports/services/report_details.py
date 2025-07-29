from django.shortcuts import render
from django.core.paginator import Paginator
from django.contrib import messages
from django.utils.dateparse import parse_date, parse_time

from datetime import datetime

from reports.extra_functions import *
from reports.models import MeasurementType, Measurement, Sensor


class ReportDetailsView:
    def __init__(self, request):
        self.request = request
        self.date_start = parse_date(request.GET.get('date_s'))
        self.date_end = parse_date(request.GET.get('date_e'))
        self.time_start = parse_time(request.GET.get('time_s'))
        self.time_end = parse_time(request.GET.get('time_e'))
        self.sensor_ids = request.GET.getlist('sensor_id')

    def report_details(self):
        start = format_date(datetime.combine(self.date_start, self.time_start))
        end = format_date(datetime.combine(self.date_end, self.time_end))
        sensors = Sensor.objects.filter(id__in=self.sensor_ids)
        types = MeasurementType.objects.filter(sensor__in=sensors).values('id', 'label', 'code').distinct()
        data = Measurement.objects.filter(date__range=(start, end), sensor__in=sensors).order_by('date') \
            .values('date', 'value', 'type', 'sensor', 'id')

        statistics = {}
        for sensor in sensors:
            statistics[f'{sensor.location}: {sensor.name}'] = {}
            for type in sensor.supported_types.all():
                statistics[f'{sensor.location}: {sensor.name}'][type.label] = calculate_stat(sensor, type, data,
                                                                                             end - start)

        measurements = {}
        for d in data:
            if (d['date'], d['sensor']) not in measurements:
                measurements[(d['date'], d['sensor'])] = []
            measurements[(d['date'], d['sensor'])].append(d)

        if self.request.method == 'POST':
            self.post(measurements, types)

        if not isinstance(measurements, list):
            measurements = list(measurements.items())

        paginator = Paginator(measurements, 200)
        page = self.request.GET.get('page')
        paged_measurements = paginator.get_page(page)

        context = {
            'start': start,
            'end': end,
            'paged_measurements': paged_measurements,
            'sensors': sensors,
            'measurement_types': types,
            'url': get_url(self.request.GET.copy()),
            'statistics': statistics,
        }
        return render(self.request, 'reports/report_details.html', context)


    def post(self, measurements, types):
        action = self.request.POST.get('action')

        if action == 'filter':
            type = self.request.POST.get('filter')
            order = (self.request.POST.get('order') == 'desc')
            for m in types:
                if m["id"] == type:
                    type = m

            sorting_key = (
                lambda x: next(((y['value'] or 0) for y in x[1] if y.type == type), 0)) if type in types else lambda \
                    x: \
                x[0]
            measurements = sorted(list(measurements.items()), key=sorting_key, reverse=order)
        elif action == 'create':
            sensor_id = self.request.POST.get('sensor_id')

            if Sensor.objects.filter(id=sensor_id).exists():
                sensor = Sensor.objects.get(id=sensor_id)
                measurement_types = sensor.supported_types.all()
                date = self.request.POST.get('date')

                if Measurement.objects.filter(date=format_date(date), sensor=sensor).exists():
                    messages.error(self.request, 'Данные уже существуют')
                else:
                    for type in measurement_types:
                        value = float(self.request.POST.get(f'{type.code}').replace(',', '.'))
                        instance = Measurement(date=format_date(date), sensor=sensor, type=type, value=value)
                        instance.save()