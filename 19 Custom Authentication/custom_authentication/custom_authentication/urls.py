"""
190923, Tuesday, 07.00 pm  
19. Custom Authentication in DRF 
"""
from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls')),
]
