from django.http import JsonResponse


def is_image(uploaded_file):
    if not uploaded_file:
        return JsonResponse({'status': 'error', 'message': 'No file provided'}, status=400)

    if not uploaded_file.content_type.startswith('image/'):
        return JsonResponse({'status': 'error', 'message': 'Only image files allowed'}, status=400)

    # ✅ Optionally check file size (example: max 10MB)
    if uploaded_file.size > 10 * 1024 * 1024:
        return JsonResponse({'status': 'error', 'message': 'File too large'}, status=400)

    return True