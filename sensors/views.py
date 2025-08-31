from django.shortcuts import render

# Create your views here.

def add_settings(request):
    return render(request, 'sensors/add_settings.html')


def add_dev_settings(request):
    return render(request, 'sensors/add_dev_settings.html')