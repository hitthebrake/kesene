from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='authorization:login')
def index(request):
    return render(request, 'reports/menu.html')