from django.urls import path
from . import views

app_name = 'reports'
urlpatterns = [
    path('', views.menu, name='menu'),
    path('archive/', views.report_archive, name='archive'),
    path('report_details/', views.report_details, name='details'),
    path('get-sensors/', views.get_sensors, name='get-sensors'),
    path('update_measurements/', views.update_measurements, name='update-measurements'),
    path('delete_measurements/', views.delete_measurements, name='delete-measurements'),
    path('thresholds/', views.thresholds, name='thresholds'),
    path('get-threshold-types/', views.get_threshold_types, name='get-threshold-types'),
]