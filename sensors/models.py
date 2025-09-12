from django.db import models

from kesene import settings
from webhook.models import Sensor


# Create your models here.
class SensorSettings(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    type_name = models.CharField(max_length=255)

    from_value = models.DecimalField(max_digits=10, decimal_places=2)
    to_value = models.DecimalField(max_digits=10, decimal_places=2)
    action = models.CharField(max_length=510)
    status = models.CharField(max_length=55)

    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class SensorNotification(models.Model):
    setting = models.ForeignKey(SensorSettings, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    progres = models.CharField(max_length=55)
