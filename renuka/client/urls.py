from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home_view),
    path('costumes/', costumes_view),
    path('accessories/', accessories_view),
    path('ornaments/', ornaments_view),
    path('forms/', form_view),
]
