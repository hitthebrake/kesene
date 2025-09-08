from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

from django.db.models.signals import post_save
from django.dispatch import receiver

from webhook.models import Measurement, Sensor, ExampleMeasurement
from webhook.sensor_parsing import sensor_types


@receiver(post_save, sender=Measurement, dispatch_uid='monitor_update')
def monitor_update(sender, instance, created, **kwargs):
    print('New measurement signal fired!!!')
    if created:
        sensor_id = instance.sensor_id
        value1 = str(round(float(instance.value1), 2)).replace('.', ',') if instance.value1 is not None else '#NV',
        value2 = str(round(float(instance.value2), 2)).replace('.', ',') if instance.value2 is not None else '#NV',
        value3 = str(round(float(instance.value3), 2)).replace('.', ',') if instance.value3 is not None else '#NV',

        sensor = Sensor.objects.get(id=sensor_id)
        types = sensor_types.get(sensor.sensor_type)
        data = {
            'sensor_id': sensor_id,
            'value1': value1 if len(types)>0 else '',
            'value2': value2 if len(types)>1 else '',
            'value3': value3 if len(types)>2 else '',
            'spot': sensor.spot,
            'name': sensor.name,
            'location': sensor.location,
            'sensor_type': sensor.sensor_type,
            'type1': f' {types[0][1]}' if len(types)>0 and value1 != '#NV' else '',
            'type2': f' {types[1][1]}' if len(types)>1 and value2 != '#NV' else '',
            'type3': f' {types[2][1]}' if len(types)>2 and value3 != '#NV' else '',
            'status': """<div class="badge fs-10 badge-phoenix badge-phoenix-success">
                            <a data-bs-target="#nodata">
                                <span class="fw-bold">Норма</span>
                                <span class="ms-1 fas fa-check"
                                      data-fa-transform="shrink-2">
                                </span>
                            </a>
                        </div>"""
        }

        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "monitor",
            {
                "type": "send_measurement",
                "data": data,
            }
        )
