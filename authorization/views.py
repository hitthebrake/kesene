from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
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

def signup(request):
    if request.user.is_authenticated:
        return redirect('reports:menu')
    if request.method == 'POST':
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.error(request, "Пароли не совпадают*")
        elif User.objects.filter(username=email).exists():
            messages.error(request, "Электронная почта уже используется*")
        else:
            user = User.objects.create_user(username=email, email=email, password=password1)
            login(request, user)
            return redirect('reports:menu')
    return render(request, 'authorization/signup.html')