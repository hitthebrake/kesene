from django.urls import path

from . import views

app_name = 'webhook'

urlpatterns = [
    path('accept_data', views.webhook, name='webhook'),
]
