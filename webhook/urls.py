from django.urls import path

from . import views

app_name = 'webhook'

urlpatterns = [
    path('accept_data/', views.webhook, name='webhook'),
    path('copy_all_data/', views.copy_all_data2, name='copy_all_data'),


]
