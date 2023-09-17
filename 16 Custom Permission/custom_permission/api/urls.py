
from argparse import Namespace
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import StudentModelViewSet, StudentReadOnlyModelViewSet # StudentViewSetAPI

router = DefaultRouter()

# router.register('studentapi', StudentViewSetAPI,  basename='studentapi')   # using viewset 

# no need to add slash after the url path 
router.register('crud/studentapi', StudentModelViewSet,  basename='crud_studentapi')   # using modelviewset 
router.register('list/studentapi', StudentReadOnlyModelViewSet,  basename='read_only_studentapi')   # using readonlymodelviewset 


urlpatterns = [

        path('', include(router.urls)),
        path('auth/', include('rest_framework.urls', namespace='rest_framework')), # this allows auth in the browsable api auth feature if other than basic auth is used 
]

