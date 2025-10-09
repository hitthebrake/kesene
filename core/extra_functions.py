from django.http import JsonResponse
from webhook.sensor_parsing import _get_sensor_types_

def is_image(uploaded_file):
    if not uploaded_file:
        return JsonResponse({'status': 'error', 'message': 'No file provided'}, status=400)

    if not uploaded_file.content_type.startswith('image/'):
        return JsonResponse({'status': 'error', 'message': 'Only image files allowed'}, status=400)

    # ✅ Optionally check file size (example: max 10MB)
    if uploaded_file.size > 10 * 1024 * 1024:
        return JsonResponse({'status': 'error', 'message': 'File too large'}, status=400)

    return True


def is_active(user):
    if not user.is_authenticated or not user.is_active or user.is_deleted:
        return False
    return True


def can_add_settings(user):
    return user.can_add_settings or user.is_superuser


def is_admin(user):
    return user.is_admin or user.is_superuser


def can_add_data(user):
    return user.can_add_data or user.is_superuser


def get_parameter_sign(sensor_type, parameter):
    list_of_types = _get_sensor_types_(sensor_type)
    if list_of_types is None:
        return ''

    for t in list_of_types:
        if t[0] == parameter:
            return t[1]

    return ''
