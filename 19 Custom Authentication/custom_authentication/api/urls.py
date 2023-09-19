
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import StudentModelViewSet, StudentReadOnlyModelViewSet # StudentViewSetAPI


# for creating token (func)
from rest_framework.authtoken.views import obtain_auth_token

# custom auth class 
from .customAuthTokens import CustomAuthToken

router = DefaultRouter()

# router.register('studentapi', StudentViewSetAPI,  basename='studentapi')   # using viewset 

# no need to add slash after the url path 
router.register('crud/studentapi', StudentModelViewSet,  basename='crud_studentapi')   # using modelviewset 
router.register('list/studentapi', StudentReadOnlyModelViewSet,  basename='read_only_studentapi')   # using readonlymodelviewset 


urlpatterns = [

        path('', include(router.urls)),
        # a funciton based view to retrieve or create auth token | hitting the endpoint, will retirieve if available else create and return a token 
        path('gettoken/', obtain_auth_token, name='get_auth_token'),
        
        # Custom auth token class | return additional data of the user along with the token
        path('custom-gettoken/', CustomAuthToken.as_view(), name='custom_auth_token'),
        
]

