
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import StudentListView, StudentReadOnlyModelViewSet, StudentModelViewSet, StudentPagination





router = DefaultRouter()

router.register('crud/studentapiList', StudentListView,  basename='crud_studentapi')   
router.register('list/studentapi', StudentReadOnlyModelViewSet,  basename='read_only_studentapi')   


urlpatterns = [

        path('', include(router.urls)),
        path('custom/studentapi/', StudentPagination.as_view(),  name='crud_ok_studentapi') , 

        
]

