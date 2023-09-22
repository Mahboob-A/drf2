
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import StudentListView, StudentReadOnlyModelViewSet, StudentModelViewSet





router = DefaultRouter()


router.register('crud/studentapi', StudentListView,  basename='crud_studentapi')   
router.register('list/studentapi', StudentReadOnlyModelViewSet,  basename='read_only_studentapi')   


urlpatterns = [

        path('', include(router.urls)),

        
]

