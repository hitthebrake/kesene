from django.urls import path

from . import views

app_name = 'webhook'

urlpatterns = [
    path('accept_data/', views.webhook, name='webhook'),
    path('copy_all_data/', views.copy_all_data, name='copy_all_data'),
]
