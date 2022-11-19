from django.contrib import admin
from django.urls import path
from client.views import *
urlpatterns = [
    path('', home_view),
    path('home/', home_view),
    path('patterns/', costumes_view),
    path('accessories/', accessories_view),
    path('jewellery/', ornaments_view),
    path('form/', form_view),
]
