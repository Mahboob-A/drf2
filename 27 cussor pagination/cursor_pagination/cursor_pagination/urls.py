"""
290923, Friday, 09.30 pm  
27. LimitOffsetPagination in DRF  
"""
from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls')),
]
