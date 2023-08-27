from django.urls import path

from .views import student_detail, student_list

urlpatterns = [
        path('<int:id>/', student_detail, name='st_detail'),  # for single st data 
        path('', student_list, name='st_list'),
]
