from django.urls import path
from . import views
app_name = 'monitoring'
urlpatterns = [
    path('', views.index, name='index'),
    path('thresholds/', views.thresholds_view, name='thresholds'),
    path('get-types/', views.get_types, name='get-types'),
    path('delete_threshold/', views.delete_threshold, name='delete-threshold'),
    path('add_data_manually/', views.add_data_manually, name='add-data-manually'),
    path('settings_view/', views.settings_view, name='settings_view'),
]