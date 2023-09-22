"""
220923, Friday, 07.00 pm  
22. django-filter in DRF  
"""
from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls')),
]
