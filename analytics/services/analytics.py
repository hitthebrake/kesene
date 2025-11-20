from datetime import datetime, date, timedelta

from django.db import connection
from django.db.models import Min, Max, Avg

from webhook.models import Sensor, Measurement
from webhook.sensor_parsing import sensor_types as webhook_st


class GetAnalytics:
    def __init__(self, request):
        self.request = request
        today = date.today()
        self.date_range = [date(today.year, today.month, 1), date(today.year, today.month, today.day)]
        self.start_date = date(today.year, today.month, 1)
        self.end_date = date(today.year, today.month, today.day)
        self.location = request.GET.get('location', 'Казандык. М-куп. пространство')
        self.stats = ['min', 'max', 'avg']
        self.value_fields = ['value1', 'value2', 'value3']

    @staticmethod
    def parse_flatpicker_date(date_str):
        return [datetime.strptime(i.strip(), "%d/%m/%Y").date() for i in date_str.split('—')]

    def get_data_from_db(self, sensor_ids):
        base_filter = {
            'date__range': (self.start_date, self.end_date),
            'sensor_id__in': sensor_ids
        }

        annotations = {}
        for i, field in enumerate(self.value_fields):
            annotations.update({
                f'min_val_{i}': Min(field),
                f'max_val_{i}': Max(field),
                f'avg_val_{i}': Avg(field),
            })

        agg_results = {}
        aggs = Measurement.objects.filter(**base_filter).values('sensor_id').annotate(**annotations)

        for row in aggs:
            sid = row['sensor_id']
            agg_results[sid] = {}
            for i in range(3):
                agg_results[sid][i] = {
                    'min_val': row[f'min_val_{i}'],
                    'max_val': row[f'max_val_{i}'],
                    'avg': row[f'avg_val_{i}'],
                    'min_date': None,  # Will be populated in next step
                    'max_date': None,  # Will be populated in next step
                }

        for i, field in enumerate(self.value_fields):
            min_dates_query = f"""
                    SELECT m1.sensor_id, m1.date
                    FROM (
                        SELECT sensor_id, MIN({field}) as min_val
                        FROM {Measurement._meta.db_table}
                        WHERE date BETWEEN %s AND %s AND sensor_id IN %s AND {field} IS NOT NULL
                        GROUP BY sensor_id
                    ) as min_vals
                    JOIN {Measurement._meta.db_table} m1 
                    ON m1.sensor_id = min_vals.sensor_id 
                       AND m1.{field} = min_vals.min_val
                       AND m1.date BETWEEN %s AND %s
                    ORDER BY m1.date
                    """

            with connection.cursor() as cursor:
                cursor.execute(min_dates_query, [self.start_date, self.end_date, tuple(sensor_ids), self.start_date, self.end_date])
                min_dates_rows = cursor.fetchall()

            for sensor_id, min_date in min_dates_rows:
                if sensor_id in agg_results and i in agg_results[sensor_id]:
                    agg_results[sensor_id][i]['min_date'] = min_date

            max_dates_query = f"""
                    SELECT m1.sensor_id, m1.date
                    FROM (
                        SELECT sensor_id, MAX({field}) as max_val
                        FROM {Measurement._meta.db_table}
                        WHERE date BETWEEN %s AND %s AND sensor_id IN %s AND {field} IS NOT NULL
                        GROUP BY sensor_id
                    ) as max_vals
                    JOIN {Measurement._meta.db_table} m1 
                    ON m1.sensor_id = max_vals.sensor_id 
                       AND m1.{field} = max_vals.max_val
                       AND m1.date BETWEEN %s AND %s
                    ORDER BY m1.date
                    """

            with connection.cursor() as cursor:
                cursor.execute(max_dates_query, [self.start_date, self.end_date, tuple(sensor_ids), self.start_date, self.end_date])
                max_dates_rows = cursor.fetchall()

            for sensor_id, max_date in max_dates_rows:
                if sensor_id in agg_results and i in agg_results[sensor_id]:
                    agg_results[sensor_id][i]['max_date'] = max_date

        return agg_results

    def process_data(self, agg_results, sensors):
        data = {}
        sensors_qs = sensors.select_related()

        for sensor in sensors_qs:
            sensor_entry = {}
            types_for_sensor = webhook_st.get(sensor.sensor_type, [])

            for i, t in enumerate(types_for_sensor):
                sensor_entry[t] = {}
                agg = agg_results.get(sensor.id, {}).get(i)
                if not agg or (agg['min_val'] is None and agg['max_val'] is None and agg['avg'] is None):
                    if "min" in self.stats:
                        sensor_entry[t]["min"] = {"value": "Нету данных", "date": "Нету данных"}
                    if "max" in self.stats:
                        sensor_entry[t]["max"] = {"value": "Нету данных", "date": "Нету данных"}
                    if "avg" in self.stats:
                        sensor_entry[t]["average"] = "Нету данных"
                    continue

                if "min" in self.stats:
                    sensor_entry[t]["min"] = {
                        "value": round(agg['min_val'], 2),
                        "date": agg['min_date']
                    }
                if "max" in self.stats:
                    sensor_entry[t]["max"] = {
                        "value": round(agg['max_val'], 2),
                        "date": agg['max_date']
                    }
                if "avg" in self.stats:
                    sensor_entry[t]["average"] = round(agg['avg'], 2) if agg['avg'] is not None else "Нету данных"

            data[sensor] = sensor_entry
        return data

    def analytics(self):
        if 'date_range' in self.request.GET:
            self.date_range = self.parse_flatpicker_date(self.request.GET['date_range'])
        self.start_date = self.date_range[0]
        self.end_date = self.date_range[-1]

        max_days = 365
        if (self.end_date - self.start_date).days > max_days:
            self.end_date = self.start_date + timedelta(days=max_days)

        sensors = Sensor.objects.all()
        if self.location != 'all':
            sensors = sensors.filter(location=self.location)

        sensor_ids = list(sensors.values_list('id', flat=True))
        types = list(sensors.values_list('sensor_type', flat=True).distinct())
        if 'location' in self.request.GET:
            active_types = self.request.GET.getlist('types')
            self.stats = self.request.GET.getlist('stats')
        else:
            active_types = list(sensors.filter(location=self.location).values_list('sensor_type', flat=True).distinct())

        sensors = sensors.filter(sensor_type__in=active_types)
        inactive_types = [t for t in types if t not in active_types]

        agg_results = self.get_data_from_db(sensor_ids)
        data = self.process_data(agg_results, sensors)

        context = {
            "cur_start_date": self.start_date,
            "cur_end_date": self.end_date,
            "cur_location": self.location,
            "active_types": active_types,
            "inactive_types": inactive_types,
            'stats': self.stats,
            'data': data,
        }
        return context