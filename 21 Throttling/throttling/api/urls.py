
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import StudentModelViewSet, StudentReadOnlyModelViewSet 





router = DefaultRouter()



# no need to add slash after the url path 
router.register('crud/studentapi', StudentModelViewSet,  basename='crud_studentapi')   
router.register('list/studentapi', StudentReadOnlyModelViewSet,  basename='read_only_studentapi')   


urlpatterns = [

        path('', include(router.urls)),

        path('auth/', include('rest_framework.urls', namespace='rest_framework')),
        
        
]

