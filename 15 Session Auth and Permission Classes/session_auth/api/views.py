

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from django.core.exceptions import ObjectDoesNotExist


from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly, DjangoObjectPermissions


from .models import Student
from .serializers import StudentSerializer




'''
Full CRUD is implamented here.
ModelViewSet inherits GenericAPIView. 
ModelViewSet also handles try catch / edge cases 
'''
'''
15.  Sesstion Authentication and Permission Classes. 
'''
class StudentModelViewSet(viewsets.ModelViewSet): 
        queryset = Student.objects.all()
        serializer_class = StudentSerializer
        
        # if authenticaed, allow all operaions, else only allow safe methods 
        # authentication_classes = [SessionAuthentication]
        # permission_classes = [IsAuthenticatedOrReadOnly]
        
        
        # DjangoModelPermissions
        # customize the HTTP request sent by the user from the admin panel. 
        # User must needed to be authenticated first - otherwise the API is not assiccalbe 
        # authentication_classes = [SessionAuthentication]
        # permission_classes = [DjangoModelPermissions]
        
        # DjangoModelPermissionsOrAnonReadOnly
        # Works as same like DjangoModelPermissions, but as DjangoModelPermissions requires the user must be authenticated to access 
        # the api, even the safe / get methods are not allowed, 
        # In the case of DjangoModelPermissionsOrAnonReadOnly, it works same like  DjangoModelPermissions but the only difference is that 
        # DjangoModelPermissionsOrAnonReadOnly allows the unauthenticated users safe / get methods. 
        authentication_classes = [SessionAuthentication]
        permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
        
        
        

        
        
        
        
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