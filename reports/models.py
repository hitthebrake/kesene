from django.core.exceptions import ValidationError
from django.db import models

class MeasurementType(models.Model):
    code = models.CharField(max_length=50, unique=True, blank=True, null=True)
    label = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.label


class Sensor(models.Model):
    name = models.CharField(max_length=100, default="Не указано", verbose_name="Название датчика")
    location = models.CharField(max_length=255, default="Не указан", verbose_name="Местонахождение датчика")
    supported_types = models.ManyToManyField(MeasurementType, verbose_name="Поддерживаемые измерения")

    def __str__(self):
        return self.name

class Measurement(models.Model):
    date = models.DateTimeField(verbose_name="Дата/время измерения", null=True, blank=True)
    type = models.ForeignKey(MeasurementType, on_delete=models.CASCADE, verbose_name="Тип измерения", blank=True, null=True)
    value = models.DecimalField(max_digits=10, decimal_places=3, verbose_name="Значение", blank=True, null=True)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, verbose_name="Датчик", blank=True, null=True)

    class Meta:
        indexes = [
            models.Index(fields=['sensor', 'type', '-date']),
        ]

    def clean(self):
        if self.type not in self.sensor.supported_types.all():
            raise ValidationError(f"{self.sensor.name} не поддерживает измерение типа {self.type.label}")

class Threshold(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    type = models.ForeignKey(MeasurementType, on_delete=models.CASCADE)
    description = models.TextField(blank=False)
    upper_limit = models.DecimalField(max_digits=10, decimal_places=3)
    lower_limit = models.DecimalField(max_digits=10, decimal_places=3)
    color = models.CharField(max_length=20)


"""
class TimeInstance(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, null=True, blank=True)

class Temperature(models.Model):
    temperature = models.DecimalField(verbose_name="Значение", max_digits=10, decimal_places=3, null=True, blank=True)

class Humidity(models.Model):
    humidity = models.DecimalField(verbose_name="Значение", max_digits=10, decimal_places=3, null=True, blank=True)

class AirFlowSpeed(models.Model):
    speed = models.DecimalField(verbose_name="Значение", max_digits=10, decimal_places=3, null=True, blank=True)

class HeatFluxDensity(models.Model):
    density = models.DecimalField(verbose_name="Значение", max_digits=10, decimal_places=3, null=True, blank=True)

class DewPoint(models.Model):
    temperature = models.DecimalField(verbose_name="Значение", max_digits=10, decimal_places=3, null=True, blank=True)

class WindDirection(models.Model):
    direction = models.IntegerField(verbose_name="Значение", null=True, blank=True)

class CO2Concentration(models.Model):
    concentration = models.DecimalField(verbose_name="Значение", max_digits=10, decimal_places=3, null=True, blank=True)

class NoiseLevel(models.Model):
    level = models.DecimalField(verbose_name="Значение", max_digits=10, decimal_places=3, null=True, blank=True)

class XSlope(models.Model):
    slope = models.DecimalField(verbose_name="Значение", max_digits=10, decimal_places=3, null=True, blank=True)

class YSlope(models.Model):
    slope = models.DecimalField(verbose_name="Значение", max_digits=10, decimal_places=3, null=True, blank=True)

class GroundWaterLevel(models.Model):
    level = models.DecimalField(verbose_name="Значение", max_digits=10, decimal_places=3, null=True, blank=True)

class BatteryLevel(models.Model):
    level = models.DecimalField(verbose_name="Значение", max_digits=10, decimal_places=3, null=True, blank=True)

class Pressure(models.Model):
    pressure = models.DecimalField(verbose_name="Значение", max_digits=10, decimal_places=3, null=True, blank=True)

class WindSpeed(models.Model):
    speed = models.DecimalField(verbose_name="Значение", max_digits=10, decimal_places=3, null=True, blank=True)

class Precipitation(models.Model):
    precipitation = models.DecimalField(verbose_name="Значение", max_digits=10, decimal_places=3, null=True, blank=True)
"""