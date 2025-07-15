from django.urls import path
from .views import MeasurementBulkCreate

urlpatterns = [
    path("api/v1/measurements/bulk/", MeasurementBulkCreate.as_view()),
]
