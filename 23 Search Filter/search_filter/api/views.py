

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from django.core.exceptions import ObjectDoesNotExist

from .models import Student
from .serializers import StudentSerializer

# permission class 
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# authentication classes 
from rest_framework.authentication import SessionAuthentication 


#  from django_filters
#  It matches the exact keyword with the fields. matches exact values 
from django_filters.rest_framework import DjangoFilterBackend  

# This is a general searching. The selected fields will be considered to search values 
# This will search any matching with the keyword with the search_fields fields. 
# matches any matching values
# it takes the search param, and returns any matching result declared based on the search_fields list. 
from rest_framework.filters import SearchFilter

'''
22. django-filter  

'''

# settings.py



# using viewset | search filter is drf's own filter 
class StudentListView(viewsets.ModelViewSet): 
        queryset = Student.objects.all()
        serializer_class = StudentSerializer 
        filter_backends = [SearchFilter, DjangoFilterBackend]
        
        filterset_fields = ['name', 'city'] # for django_filters DjangoFilterBackend  | http://127.0.0.1:8000/crud/studentapi/?name=Halim&city=Boyra
        # search_fields = ['name', 'city'] #  matches any matching with the qulery param|  drf's own search filter | http://127.0.0.1:8000/crud/studentapi/?search=Halim
        
        # search_fields = ['^name'] # matches only the first char of the field with the query param 
        search_fields = ['=name'] # matches the exact matching with the query param | case insecsitive 










class StudentModelViewSet(viewsets.ModelViewSet): 
        queryset = Student.objects.all()
        serializer_class = StudentSerializer
        
        authentication_classes = [SessionAuthentication]
        
        permission_classes = [IsAuthenticatedOrReadOnly]
        
        

        
'''
ReadOnlyModelViewSet only provides List and Retrieve (only provides GET method.)
ReadOnlyModelViewSet also inherits GenericAPIView 
'''
class StudentReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet): 
        queryset = Student.objects.all()
        serializer_class = StudentSerializer 
        
        





''' Below Code Is Using ViewSet '''

'''

list
create
retrieve 
update
partial_update 
destroy 



class StudentViewSetAPI(viewsets.ViewSet): 
        
        def list(self, request): 
                students = Student.objects.all()
                serializer = StudentSerializer(students, many=True)
                return Response({'data' : serializer.data}, status=status.HTTP_200_OK)
                # return Response(serializer.data, status=status.HTTP_200_OK)
        
        def create(self, request): 
                serializer = StudentSerializer(data=request.data)
                if serializer.is_valid(): 
                        serializer.save()
                        return Response({'data' : serializer.data}, status=status.HTTP_201_CREATED)
                return Response({'error' : serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
        def retrieve(self, request, pk=None): 
                try: 
                        student = Student.objects.get(pk=pk)
                        serializer = StudentSerializer(student)
                        return Response({'data' : serializer.data}, status=status.HTTP_200_OK)
                except ObjectDoesNotExist: 
                        return Response({'error' : f'The ID {pk} Is Invalid !!'}, status=status.HTTP_400_BAD_REQUEST)
                
        def update(self, request, pk=None): 
                try: 
                        student = Student.objects.get(pk=pk)
                        serializer = StudentSerializer(student, data=request.data)
                        if serializer.is_valid(): 
                                serializer.save()
                                return Response({'data' : serializer.data}, status=status.HTTP_200_OK)
                        return Response({'error' : serializer.errors}, status=status.HTTP_304_NOT_MODIFIED)
                
                except ObjectDoesNotExist: 
                        return Response({'error' : f'The ID {pk} Is Invalid !!'}, status=status.HTTP_400_BAD_REQUEST)
                
                
        def partial_update(self, request, pk=None): 
                try: 
                        student = Student.objects.get(pk=pk)
                        serializer = StudentSerializer(student, data=request.data, partial=True)
                        if serializer.is_valid(): 
                                serializer.save()
                                return Response({'data' : serializer.data}, status=status.HTTP_200_OK)
                        return Response({'error' : serializer.errors}, status=status.HTTP_304_NOT_MODIFIED)
                
                except ObjectDoesNotExist: 
                        return Response({'error' : f'The ID {pk} Is Invalid !!'}, status=status.HTTP_400_BAD_REQUEST)
                        
        
        def destroy(self, request, pk=None): 
                try: 
                        student = Student.objects.get(pk=pk)
                        name = student.name 
                        student.delete()
                        return Response({'data' : f'The Student - {name.upper} With ID {pk} Is Deleted !!'}, status=status.HTTP_204_NO_CONTENT)     
                except ObjectDoesNotExist:    
                        return Response({'error' : f'The ID {pk} Is Invalid !!'}, status=status.HTTP_400_BAD_REQUEST)
                        
                        
'''