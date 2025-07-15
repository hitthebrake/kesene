from django.db import models


class Sensor(models.Model):
    file_name   = models.CharField(max_length=255)
    group_name  = models.CharField(max_length=255)
    channels    = models.PositiveIntegerField()
    description = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = ("file_name", "group_name")

    def __str__(self):
        return f"{self.file_name} :: {self.group_name}"


class Measurement(models.Model):
    sensor      = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    recorded_at = models.DateTimeField()

    temperature_c        = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    humidity_percent     = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    dew_point_c          = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    pressure_mmhg        = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    wind_speed_mps       = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    wind_direction_deg   = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    precipitation_mm     = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    noise_level_db       = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    groundwater_level_m  = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    airflow_speed_mps    = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    tilt_x_deg           = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    tilt_y_deg           = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    battery_voltage_v    = models.DecimalField(max_digits=6, decimal_places=3, null=True, blank=True)

    class Meta:
        unique_together = ("sensor", "recorded_at")
        ordering = ["recorded_at"]
