
from django.contrib import admin
from django.urls import path, include
from public.views import *

urlpatterns = [
    # path('', home_page),
    # path("", home_page, name ="admin"),
    path('', view_listings_page)
]