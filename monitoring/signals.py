from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

from django.db.models.signals import post_save
from django.dispatch import receiver

from sensors.models import SensorSettings
from webhook.models import Measurement, Sensor, ExampleMeasurement
from webhook.sensor_parsing import sensor_types
from monitoring.services.index import check_limits, compare_status


@receiver(post_save, sender=Measurement, dispatch_uid='monitor_update')
def monitor_update(sender, instance, created, **kwargs):
    # print('New measurement signal fired!!!')
    if created:
        sensor_id = instance.sensor_id
        value1 = str(round(float(instance.value1), 2)).replace('.', ',') if instance.value1 is not None else '#NV'
        value2 = str(round(float(instance.value2), 2)).replace('.', ',') if instance.value2 is not None else '#NV'
        value3 = str(round(float(instance.value3), 2)).replace('.', ',') if instance.value3 is not None else '#NV'

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
            'type1': f' {types[0][1]}' if (len(types)>0 and value1 != '#NV') else '',
            'type2': f' {types[1][1]}' if (len(types)>1 and value2 != '#NV') else '',
            'type3': f' {types[2][1]}' if (len(types)>2 and value3 != '#NV') else '',
            'setting': {'status': 'Норма'},
            'sensor_image': sensor.image.url if sensor.image else None,
        }

        sensor_settings = SensorSettings.objects.filter(sensor_id=sensor_id)
        for i in range(len(types)):
            for s in sensor_settings:
                if s.type_name == types[i][0]:
                    if check_limits(s, data[f'value{i + 1}']):
                        status = compare_status(data['setting']['status'], s.status)
                        if status == s.status:
                            data['setting'] = {
                                'status': s.status,
                                'id': s.id,
                                'action': s.action,
                            }

        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "monitor",
            {
                "type": "send_measurement",
                "data": data,
            }
        )
