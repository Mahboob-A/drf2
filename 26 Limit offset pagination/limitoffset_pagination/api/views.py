

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


from rest_framework.filters import OrderingFilter 
from rest_framework.filters import SearchFilter



# custom pagination 
from .pagination import DemoPagination 

from rest_framework.views import APIView

'''
25. PageNumberPagination  

'''



# using viewset | search filter is drf's own filter 
class StudentListView(viewsets.ModelViewSet): 
        queryset = Student.objects.all()
        serializer_class = StudentSerializer 
        filter_backends = [SearchFilter, OrderingFilter]
        search_fields = ['name', ]
        ordering_fields = ['name', 'city']  # see settngs.py for changed param 
        
        # paginaition 
        pagination_class = DemoPagination 



class StudentPagination(APIView):
        def get(self, request, format=None): 
                students = Student.objects.all()
                limit = request.query_params.get('limit', None)
                
                # 
                # if limit: 
                #         paginator = DemoPagination()
                #         paginator.default_limit = limit 
                # else: 
                #         paginator = DemoPagination()
                
                print('limit: ', limit)
                paginator = DemoPagination()
                paginated_page = paginator.paginate_queryset(students, request, view=self)
                serializer = StudentSerializer(paginated_page, many=True)
                return paginator.get_paginated_response(serializer.data)






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