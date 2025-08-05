from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

from django.db.models.signals import post_save
from django.dispatch import receiver

from reports.models import Measurement
from reports.models import Threshold

@receiver(post_save, sender=Measurement, dispatch_uid='data_saved')
def data_saved(sender, instance, created, **kwargs):
    print('Signal fired!!!')
    if created:
        thresholds = Threshold.objects.select_related('sensor', 'type').values(
            'id', 'color',
            'sensor__id', 'type__id',
            'sensor__name', 'sensor__location',
            'type__label', 'type__code',
            'description', 'upper_limit', 'lower_limit'
        )
        sensor_id = int(instance.sensor_id)
        type_id = int(instance.type_id)
        value = None
        if instance.value is not None:
            value = float(instance.value)

        data = {
            'sensor_id': sensor_id,
            'type_id': type_id,
            'value': value,
            'label': instance.type.label,
            'code': instance.type.code,
            'color' : '#32CD32',
            'description': 'Все нормально!',
        }
        for threshold in thresholds:
            print(threshold)
            if threshold['sensor__id'] == sensor_id and threshold['type__id'] == type_id:
                if value is not None and threshold['upper_limit'] > value >= threshold['lower_limit']:
                    data['color'] = threshold['color']
                    data['description'] = threshold['description']

        print('signals:', data)

        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "monitor",
            {
                "type": "send_measurement",
                "data": data,
            }
        )