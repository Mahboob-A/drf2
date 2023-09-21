
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import StudentModelViewSet, StudentReadOnlyModelViewSet

from rest_framework.authtoken.views import obtain_auth_token

# Importing the SimpleJWT views 
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView 

router = DefaultRouter()

# router.register('studentapi', StudentViewSetAPI,  basename='studentapi')   # using viewset 

# no need to add slash after the url path 
router.register('studentapi', StudentModelViewSet,  basename='crud_studentapi')   # using modelviewset 
router.register('list/studentapi', StudentReadOnlyModelViewSet,  basename='read_only_studentapi')   # using readonlymodelviewset 


urlpatterns = [

        path('', include(router.urls)),
        
        path('gettoken/', obtain_auth_token, name='authtoken'),
        # adding the simple jwt viwes in path 
        path('get-token/', TokenObtainPairView.as_view(), name='get_token'),
        path('refresh-token/', TokenRefreshView.as_view(), name='token_refresh'),
        path('token-verify/', TokenVerifyView.as_view(), name='token_veryfy'),


        
]

