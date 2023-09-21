"""
210923, Thursday, 07.00 pm  
21. Throttling in DRF  
"""
from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls')),
]
