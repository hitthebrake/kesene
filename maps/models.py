from django.db import models
from webhook.models import Sensor


class Coordinate(models.Model):
    sensor = models.OneToOneField(Sensor, on_delete=models.CASCADE)
    x = models.DecimalField(decimal_places=5, max_digits=10)
    y = models.DecimalField(decimal_places=5, max_digits=10)
