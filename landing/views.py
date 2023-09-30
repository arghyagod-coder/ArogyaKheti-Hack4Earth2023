from urllib.parse import urlencode
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.urls import reverse
from .forms import RegisterFIDC, LoginWithFIDC
from .models import User
import uuid
from dashboard.views import home_page

# Create your views here.
def landing_page(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        form = LoginWithFIDC(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            fidc = form.cleaned_data['fidcId']

            try: 
                loggedin = User.objects.get(name=name, fidc=fidc)
                request.session["member_logged_id"] = int(loggedin.id)
                return redirect((f'/admin/'))
            except:
                request.session["error_message"] = "Invalid Credentials"
                return redirect((f'/admin/404/'))
    else:
        form = LoginWithFIDC()
    return render(request, 'login.html', {
        'form': form
    })

def register(request):
    if request.method == 'POST':
        form = RegisterFIDC(request.POST)
        if form.is_valid():
            User.objects.create(**form.cleaned_data, fidc=uuid.uuid4())
            fidc = User.objects.get(phone=form.cleaned_data['phone']).fidc
            return render(request, 'login_success.html', {
                'fidc': fidc
            })
    else:
        form = RegisterFIDC()

    return render(request, 'register.html', {
        'form': form
    })
