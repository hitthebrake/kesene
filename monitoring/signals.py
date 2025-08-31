from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

from django.db.models.signals import post_save
from django.dispatch import receiver

from webhook.models import ExampleMeasurement, Sensor


@receiver(post_save, sender=ExampleMeasurement, dispatch_uid='monitor_update')
def monitor_update(sender, instance, created, **kwargs):
    print('New measurement signal fired!!!')
    if created:
        sensor_id = instance.sensor_id
        value1 = round(float(instance.value1), 2) if instance.value1 is not None else '#NV',
        value2 = round(float(instance.value2), 2) if instance.value2 is not None else '#NV',
        value3 = round(float(instance.value3), 2) if instance.value3 is not None else '#NV',

        sensor = Sensor.objects.get(id=sensor_id)
        data = {
            'sensor_id': sensor_id,
            'value1': value1,
            'value2': value2,
            'value3': value3,
            'spot': sensor.spot,
            'name': sensor.name,
            'location': sensor.location,
            'sensor_type': sensor.sensor_type,
        }

        print('signals:', data)

        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "monitor",
            {
                "type": "send_measurement",
                "data": data,
            }
        )
