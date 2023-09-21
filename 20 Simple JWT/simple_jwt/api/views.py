

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from django.core.exceptions import ObjectDoesNotExist

from .models import Student
from .serializers import StudentSerializer


# Somple JWT 
from rest_framework_simplejwt.authentication import JWTAuthentication

# Permissions 
from rest_framework.permissions import IsAuthenticated





'''
19. Custom Authentication 
We are using custom authenticaiton class, subclassing rest_framework.authentication import BaseAuthentication 

'''
class StudentModelViewSet(viewsets.ModelViewSet): 
        queryset = Student.objects.all()
        serializer_class = StudentSerializer
        
        # Token Authentication | Token is created by a signal 
        authentication_classes = [JWTAuthentication]
        
        # Only allowing the authenticated users. 
        permission_classes = [IsAuthenticated]
      
      
      
      
'''
ReadOnlyModelViewSet only provides List and Retrieve (only provides GET method.)
ReadOnlyModelViewSet also inherits GenericAPIView 
'''
class StudentReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet): 
        queryset = Student.objects.all()
        serializer_class = StudentSerializer 
        
        
        

