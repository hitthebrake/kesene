from django.urls import path
from analytics import views

app_name = "analytics"
urlpatterns = [
    path('', views.analytics, name='analytics'),
    path('get_location_info/<str:location>/', views.get_location_info, name='get_location_info'),
]