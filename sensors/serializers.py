from rest_framework import serializers
from .models import Sensor, Measurement


class MeasurementSerializer(serializers.ModelSerializer):
    # extra fields coming from the client
    file_name  = serializers.CharField(write_only=True)
    group_name = serializers.CharField(write_only=True)
    channels   = serializers.IntegerField(write_only=True, required=False)

    class Meta:
        model  = Measurement
        fields = "__all__"
        read_only_fields = ("sensor",)

    def create(self, validated):
        file_name  = validated.pop("file_name")
        group_name = validated.pop("group_name")
        channels   = validated.pop("channels", None)

        sensor, created = Sensor.objects.get_or_create(
            file_name=file_name,
            group_name=group_name,
            defaults={"channels": channels or 1},
        )
        if not created and channels is not None and sensor.channels != channels:
            sensor.channels = channels          # keep channels up-to-date
            sensor.save(update_fields=["channels"])

        validated["sensor"] = sensor
        return super().create(validated)
