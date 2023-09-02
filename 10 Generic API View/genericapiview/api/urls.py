
from django.urls import path 

from . import views


urlpatterns = [
        # define two urls one for get all, one for get particular data with id for the same view 
        path('people/', views.GetCreatePeopleAPI.as_view(), name='people_api'),
        path('people/<int:pk>/', views.RetriveUpdateDeletePeopleAPI.as_view(), name='people_api'),
]
