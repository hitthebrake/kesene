from django.db import models

from kesene import settings
from webhook.models import Sensor


# Create your models here.
class SensorSettings(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    type_name = models.CharField(max_length=255)

    from_value = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    to_value = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    action = models.CharField(max_length=510)
    status = models.CharField(max_length=55)

    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class SensorNotification(models.Model):
    setting = models.ForeignKey(SensorSettings, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    progres = models.CharField(max_length=55)


class ManualData(models.Model):
    location = models.CharField(max_length=255)
    local_temperature = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add=True)
    is_draft = models.BooleanField(default=False)

    class Meta:
        indexes = [
            models.Index(fields=['location', '-created_date']),
        ]


class InstanceManualData(models.Model):
    number = models.CharField(max_length=3, default='1')
    manual_data = models.ForeignKey(ManualData, on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    img = models.ImageField(upload_to='manual_data/', null=True, blank=True)
    type_name = models.CharField(max_length=255)
    created_time = models.TimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['manual_data', 'type_name']),
        ]
