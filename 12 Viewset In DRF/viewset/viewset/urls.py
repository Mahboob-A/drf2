
'''
12: Viewset in DRF 
110923, Monday, 06.30 am 
'''


from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls')),
]
