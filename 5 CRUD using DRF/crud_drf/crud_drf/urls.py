"""
CRUD app using RDF 
240823, Thursday, 06.30 am 
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]
