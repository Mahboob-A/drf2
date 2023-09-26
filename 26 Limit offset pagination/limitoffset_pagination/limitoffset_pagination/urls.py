"""
260923, Tuesday, 07.00 pm  
26. LimitOffsetPagination in DRF  
"""
from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls')),
]
