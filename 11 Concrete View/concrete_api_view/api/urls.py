
from django.urls import path 

from . import views


# Concrete APIVIew (inherits GenericAPIView and Model Mixins)
urlpatterns = [
        
        # multi classes 
        path('people/', views.PeopleListCreateAPI.as_view(), name='people_api'),

        # path('people/<int:pk>/', views.PeopleRetriveUpdateAPI.as_view(), name='people_api'),
        # path('people/<int:pk>/', views.PeopleRetriveDestroyAPI.as_view(), name='people_api'),
        path('people/<int:pk>/', views.PeopleRetriveUpdateDestroyAPI.as_view(), name='people_api'),
        
        
        # single classes 
        # path('people/', views.PeopleListAPI.as_view(), name='people_api'),
        # path('people/', views.PeopleCreateAPI.as_view(), name='people_api'),
        
        # path('people/<int:pk>/', views.PeopleRetriveAPI.as_view(), name='people_api'),
        # path('people/<int:pk>/', views.PeopleUpdateAPI.as_view(), name='people_api'),
        # path('people/<int:pk>/', views.PeopleDestroyAPI.as_view(), name='people_api'),
]




# For GenericAPIView and Model Mixins 
# urlpatterns = [
#         # define two urls one for get all, one for get particular data with id for the same view 
#         path('people/', views.GetCreatePeopleAPI.as_view(), name='people_api'),
#         path('people/<int:pk>/', views.RetriveUpdateDeletePeopleAPI.as_view(), name='people_api'),
# ]
