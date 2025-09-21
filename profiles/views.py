from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from authorization.models import CustomUser
# Create your views here.

@login_required(login_url='authorization:login')
def profile(request):
    user_id = request.user.id
    user = CustomUser.objects.get(id=user_id)
    if user.is_superuser:
        user.can_add_data = True
        user.can_create_user = True
        user.can_add_threshold = True
        user.save()

    data = {
        'id': user.id,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
        'is_superuser': user.is_superuser,
        'can_add_threshold': user.can_add_threshold,
        'can_add_data': user.can_add_data,
        'can_create_user': user.can_create_user,
        'phone': user.phone,
    }

    return render(request, 'profiles/profile.html', data)
