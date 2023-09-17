

'''
16. Custom Permission In DRF  
170923, Sunday, 03.30 pm 
'''
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls')),
]
