from django.urls import path
from . import views
app_name = 'monitoring'
urlpatterns = [
    path('', views.index, name='index'),
    path('thresholds/', views.thresholds_view, name='thresholds'),
    path('get-types/', views.get_types, name='get-types'),

]