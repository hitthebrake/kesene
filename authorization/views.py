from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import CustomUser
# Create your views here.

def login_view(request):
    if request.user.is_authenticated:
        return redirect('reports:menu')
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('reports:menu')

        messages.error(request, 'Недействительная электронная почта или неправильный пароль')
    return render(request, 'authorization/login.html')

@login_required(login_url='authorization:login')
def logout_view(request):
    logout(request)
    return redirect('authorization:login')

@login_required(login_url='authorization:login')
def signup(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        role = request.POST.get('role')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.error(request, "Пароли не совпадают*")
        elif CustomUser.objects.filter(email=email).exists():
            messages.error(request, "Электронная почта уже используется*")
        else:
            user = CustomUser.objects.create_user(
                username=email,
                email=email,
                password=password1,
                phone=phone,
                first_name=first_name,
                last_name=last_name
            )
            messages.success(request, 'Пользователь успешно создан')
    return render(request, 'authorization/signup.html')