from django.urls import path, include

import authorization
from . import views
urlpatterns = [
    path('', include('authorization.urls')),
    path('main/', include('reports.urls')),
    path('monitoring/', include('monitoring.urls')),
    path('profile/', include('profiles.urls')),
    path('maps/', include('maps.urls')),
    path('webhook/', include('webhook.urls')),
]