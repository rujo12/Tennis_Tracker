from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def login_view(request):
    return render(request, 'frontend/login.html')

@login_required
def dashboard(request):
    return render(request, 'frontend/dashboard.html')

@login_required
def favourites(request):
    return render(request, 'frontend/favourites.html')

@login_required
def schedule(request):
    return render(request, 'frontend/schedule.html')

def register_view(request):
    return render(request, 'frontend/register.html')

