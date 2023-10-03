
'''
031023, Tuesday, 08.00 pm 
29. Hyperlinked Model Serializer in DRF 
'''

from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls')),
    
]
