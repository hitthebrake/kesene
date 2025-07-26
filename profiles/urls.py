from django.urls import include, path
from . import views

app_name = 'profiles'

urlpatterns = [
    path('', views.profile, name='profile'),
]