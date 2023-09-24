"""
240923, Sunday, 07.00 pm  
23. Search Filter in DRF  
"""
from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls')),
]
