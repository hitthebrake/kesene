from django.db import models


class WebhookRequest(models.Model):
    data = models.JSONField()


class Sensor(models.Model):
    name = models.CharField(max_length=100, default="Не указано", verbose_name="Название датчика")
    location = models.CharField(max_length=255, default="Не указан", verbose_name="Местонахождение датчика")
    spot = models.CharField(max_length=100, default="", verbose_name="Точка", null=True, blank=True)
    sensor_type = models.CharField(max_length=50, default='', null=True, blank=True, verbose_name='Тип сенсора')
    image = models.ImageField(upload_to='sensor_images/', null=True, blank=True)
    def __str__(self):
        return self.name


class Measurement(models.Model):
    date = models.DateTimeField(verbose_name="Дата/время измерения", null=True, blank=True)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, verbose_name="Датчик", blank=True, null=True)

    value1 = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Значение 1", blank=True, null=True)
    value2 = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Значение 2", blank=True, null=True)
    value3 = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Значение 3", blank=True, null=True)

    class Meta:
        indexes = [
            models.Index(fields=['sensor', '-date']),
        ]


class MeteoData(models.Model):
    date = models.DateTimeField(verbose_name="Дата/время измерения", null=True, blank=True)

    temperature = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    dewpoint = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pressure = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    humidity = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    wind_speed = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    wind_direction = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    precipitation = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    class Meta:
        indexes = [
            models.Index(fields=['-date']),
        ]


class ExampleMeasurement(models.Model):
    date = models.DateTimeField(verbose_name="Дата/время измерения", null=True, blank=True)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, verbose_name="Датчик", blank=True, null=True)

    value1 = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Значение 1", blank=True, null=True)
    value2 = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Значение 2", blank=True, null=True)
    value3 = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Значение 3", blank=True, null=True)