import pandas
from django.db.models.expressions import result

from django.utils import timezone

from datetime import timedelta


def calculate_stat(sensor, t, data, duration):
    total_val, count_none, count_tot = 0, 0, 0
    maximum, minimum = -100000, 100000

    for obj in data:
        if obj['sensor'] == sensor.id and obj['type'] == t.id:
            if obj['value'] is None or obj['value'] == "":
                count_none += 1
            else:
                count_tot += 1
                total_val += obj['value']
                maximum = max(maximum, obj['value'])
                minimum = min(minimum, obj['value'])

    average = None
    if count_tot > 0:
        average = round(total_val / count_tot, 3)

    interval = 10 if 'ТвОВв' in str(sensor.name) else 2
    time_active = timedelta(minutes=count_tot * interval)

    result = {'average': average, 'max': maximum, 'min': minimum,
              'active_duration': get_str_timedelta(time_active), 'passive_duration': get_str_timedelta(duration - time_active),
              'total_count': count_tot, 'interval': interval,
              }
    return result


def format_date(date):
    res = pandas.to_datetime(date).to_pydatetime()
    return timezone.make_aware(res)


def get_url(request):
    if 'page' in request:
        del request['page']
    return request.urlencode()


def get_str_timedelta(td):
    days_str = ""
    days = td.days
    if days > 0:
        days_str = f'{days} дней, '
        if days == 1:
            days_str = "1 день, "

    hours, remainder = divmod(td.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{days_str}{hours:02}:{minutes:02}:{seconds:02}"
