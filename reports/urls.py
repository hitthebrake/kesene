from django.urls import path
from . import views

app_name = 'reports'
urlpatterns = [
    path('', views.menu, name='menu'),
    path('get-sensors/', views.get_sensors, name='get-sensors'),
    path('update_measurements/', views.update_measurements, name='update-measurements'),
    path('delete_measurements/', views.delete_measurements, name='delete-measurements'),
    path('download_excel_report/', views.download_excel_report, name='download-excel-report'),
]