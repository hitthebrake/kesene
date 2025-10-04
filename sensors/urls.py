from django.urls import path

from sensors import views

app_name = 'sensors'


urlpatterns = [
    path('add_settings/', views.add_settings, name='add_settings'),
    path('add_dev_settings/', views.add_dev_settings, name='add_dev_settings'),
    path('upload_sensor_image/<int:sensor_id>/', views.upload_sensor_image, name='upload_sensor_image'),
    path('delete_setting/', views.delete_setting, name='delete_setting'),
    path('dev_settings_list/', views.dev_settings_list, name='dev_settings_list'),
    path("get_sensors_info/<str:location>/", views.get_sensors_info, name='get_sensors_info'),
    path("scenario_list/<str:season>/", views.scenario_list, name='scenario_list'),
]