from django.db.models.signals import post_save
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.dispatch import receiver

from reports.models import MeasurementType, Measurement, Sensor

@receiver(post_save, sender=Measurement)
def notify_new_data(sender, instance, created, **kwargs):
    if created:
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "live_data",
            {
                "type": "send_new_data",
                "data": {
                    "id": instance.id,
                    "value": instance.value,
                    # Add any fields to send to frontend
                },
            },
        )
