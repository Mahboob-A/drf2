
from django.urls import path 

from .views import people_api


urlpatterns = [
        # define two urls one for get all, one for get particular data with id for the same view 
        path('people/', people_api, name='people_api'),
        path('people/<int:id>/', people_api, name='people_api'),
]
