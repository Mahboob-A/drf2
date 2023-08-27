"""
CRUD app using RDF 
7. Model Serializer in Django REST Framework
270823, Sunday, 06.45 am 
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]
