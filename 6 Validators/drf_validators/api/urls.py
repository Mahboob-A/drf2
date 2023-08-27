from django.urls import path

from .views import * 

urlpatterns = [
        path('', StudentAPI.as_view(), name='student_api'),
]
