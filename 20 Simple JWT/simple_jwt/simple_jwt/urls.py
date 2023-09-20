"""
200923, Wednesday, 08.00 pm  
20. Simple JWT Authentication in DRF 
"""
from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls')),
]
