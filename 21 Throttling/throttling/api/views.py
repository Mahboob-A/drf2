

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

# throttling 

from rest_framework.throttling import AnonRateThrottle, UserRateThrottle, ScopedRateThrottle 


# custom throttle 
from .throttling import CustomUserRateThrottle 




'''
21. Throttling 

'''
class StudentModelViewSet(viewsets.ModelViewSet): 
        queryset = Student.objects.all()
        serializer_class = StudentSerializer
        
        authentication_classes = [SessionAuthentication]
        
        permission_classes = [IsAuthenticatedOrReadOnly]
        
        # throttling 
        throttle_classes = [AnonRateThrottle, CustomUserRateThrottle]
        


'''
http => httpie package 

GET : 

http http://127.0.0.1:800/crud/studentapi/'Authorization:Token token_here' 

POST : 

http -f POST http://127.0.0.1:800/crud/studentapi/ name=abc roll=101 'Authorization:Token token_here' 

PUT : 

http PUT http://127.0.0.1:800/crud/studentapi/1/ name=abc roll=101 'Authorization:Token token_here' 

DELETE : 

http DELETE http://127.0.0.1:800/crud/studentapi/1/ 'Authorization:Token token_here' 

'''

        
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