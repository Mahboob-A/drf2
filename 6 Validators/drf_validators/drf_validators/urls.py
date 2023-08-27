"""
CRUD app using RDF 
6. Validators In Django Rest Framework 
260823, Saturday, 08.00 am 
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]
