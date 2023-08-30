
from django.urls import path 

from .views import PeopleAPI


urlpatterns = [
        # define two urls one for get all, one for get particular data with id for the same view 
        path('people/', PeopleAPI.as_view(), name='people_api'),
        path('people/<int:id>/', PeopleAPI.as_view(), name='people_api'),
]
