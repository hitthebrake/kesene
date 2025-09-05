from django.db import models

from webhook.models import Sensor


# Create your models here.
class SensorSettings(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    type_name = models.CharField(max_length=255)

    from_value = models.CharField(max_length=255)
    to_value = models.CharField(max_length=255)
    action = models.CharField(max_length=510)
    status = models.CharField(max_length=55)

    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)


class SensorNotification(models.Model):
    setting = models.ForeignKey(SensorSettings, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    progres = models.CharField(max_length=55)
