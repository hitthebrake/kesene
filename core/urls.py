from django.urls import path, include

import authorization
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('', include('authorization.urls')),
    path('main/', include('reports.urls')),
    path('monitoring/', include('monitoring.urls')),
]