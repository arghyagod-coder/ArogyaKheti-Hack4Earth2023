
from django.contrib import admin
from django.urls import path, include
from dashboard.views import *

urlpatterns = [
    path("", home_page, name ="admin"),
    path('tools/crop_recommendation', croprec),
    path('tools/fertilizer_recommendation', fertrec),
    path('forum/', forum),
    path('prices/', crop_prices_page),
    path('news/', news_page),
    path('help/', help_page),
    path('profile/', profile_page),
    path('logout/', logout_view),
    path('404/', e404_page),
    path('list_product/', list_page),
    path('check_products/', check_my_listings),
    path('delete_listing/<int:id>/', delete_listing)
]

