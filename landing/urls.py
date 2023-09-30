
from django.contrib import admin
from django.urls import path
from landing.views import landing_page, register, login

urlpatterns = [
    path('', landing_page, name="home"),
    path('login/', login, name="login"),
    path('register/', register, name="register"),
]
