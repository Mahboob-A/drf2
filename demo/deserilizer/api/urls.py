from django.urls import path
from .views import * 

urlpatterns = [
        path('stdata/', create_student, name='create_student'),
]
