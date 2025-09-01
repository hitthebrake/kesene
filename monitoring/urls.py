from django.urls import path
from . import views
app_name = 'monitoring'
urlpatterns = [
    path('', views.index, name='index'),
    path('add_data_manually/', views.add_data_manually, name='add-data-manually'),
    path('settings_view/', views.settings_view, name='settings_view'),
    # path('signal/', views.fire_signal, name='signal'),
]