
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import StudentAPI

router = DefaultRouter()

router.register('studentapi', StudentAPI,  basename='studentapi')


urlpatterns = [

        path('', include(router.urls)),
]

