from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect

from maps.models import Coordinate
from webhook.models import Sensor


# Create your views here.

@login_required(login_url='authorization:login')
def maps_view(request):
    sensors = Sensor.objects.all()
    context = {
        'first_floor': [],
        'second_floor': [],
        'third_floor': [],
    }
    for sensor in sensors:
        floor = sensor.spot[1]
        if floor == '1':
            context['first_floor'].append(sensor)
        elif floor == '2':
            context['second_floor'].append(sensor)
        elif floor == '3' or floor == '4':
            context['third_floor'].append(sensor)


    return render(request, 'maps/on_map.html', context)


def save_coordinates(request):
    if request.method == 'POST':
        x = round(float(request.POST.get('x')), 5)
        y = round(float(request.POST.get('y')), 5)
        sensor_id = request.POST.get('sensor_id')

        try:
            coordinate = Coordinate(x=x, y=y, sensor_id=sensor_id)
            coordinate.save()
        except Exception as e:
            print(e)
    return redirect('maps:maps')


def get_coordinates(request):
    coords = list(Coordinate.objects.select_related('sensor').values(
        'x', 'y', 'sensor__name', 'sensor__id', 'sensor__spot', 'sensor__sensor_type',
        'sensor__image', 'sensor__location'
    ))
    return JsonResponse(coords, safe=False)