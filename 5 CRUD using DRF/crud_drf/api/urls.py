from django.urls import path

from .views import * 

urlpatterns = [
        path('', student_api, name='student_api'),
]
