
from django.urls import path 

from .views import * 

urlpatterns = [
        path('', simple_api, name='simple_api'),
]

