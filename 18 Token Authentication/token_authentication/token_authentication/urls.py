"""
180923, Monday, 07.00 am 
18. Token Authentication in DRF 
"""
from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls')),
]
