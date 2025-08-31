from django.urls import path

from sensors import views

app_name = 'sensors'


urlpatterns = [
    path('add_settings/', views.add_settings, name='add_settings'),
    path('add_dev_settings/', views.add_dev_settings, name='add_dev_settings'),
]