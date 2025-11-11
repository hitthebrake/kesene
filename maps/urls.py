from django.urls import path
from . import views

app_name = 'maps'

urlpatterns = [
    path('', views.maps_view, name='maps'),
    path('save_coordinates/', views.save_coordinates, name='save-coordinates'),
    path('get_coordinates/', views.get_coordinates, name='get-coordinates'),
]