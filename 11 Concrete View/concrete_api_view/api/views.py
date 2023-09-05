

# For API with api_view decorator and APIViwe class 
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# For GenericAPIView and Model Mixin 
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin

# For Concrete APIViews (inherits GenericAPIView and Model Mixins)
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, ListCreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView

# other imports django imports 
from django.core.exceptions import ObjectDoesNotExist
from .models import People
from .serializer import PeopleSerializer



''' MultiClasses '''

# using the below 2 classes only, the entire curd operation is build, they contain GenericAPIView and all the Model Mixin classes inherited. 
# get all + post 
class PeopleListCreateAPI(ListCreateAPIView): 
        queryset = People.objects.all()
        serializer_class = PeopleSerializer
        

# get single + put + patch + delete  
class PeopleRetriveUpdateDestroyAPI(RetrieveUpdateDestroyAPIView): 
        queryset = People.objects.all()
        serializer_class = PeopleSerializer        


# pk needed for below all 
# get singel + put + patch 
class PeopleRetriveUpdateAPI(RetrieveUpdateAPIView): 
        queryset = People.objects.all()
        serializer_class = PeopleSerializer
        

# get single + delete 
class PeopleRetriveDestroyAPI(RetrieveDestroyAPIView): 
        queryset = People.objects.all()
        serializer_class = PeopleSerializer
        





''' Single Classes '''
class PeopleListAPI(ListAPIView): 
        queryset = People.objects.all()
        serializer_class = PeopleSerializer
        

class PeopleCreateAPI(CreateAPIView): 
        queryset = People.objects.all()
        serializer_class = PeopleSerializer        
        

# pk will be automaticaly handled, remember to receive pk in urlpatterns 

class PeopleRetriveAPI(RetrieveAPIView): 
        queryset = People.objects.all()
        serializer_class = PeopleSerializer  

class PeopleUpdateAPI(UpdateAPIView): 
        queryset = People.objects.all()
        serializer_class = PeopleSerializer  
               
        
class PeopleDestroyAPI(DestroyAPIView): 
        queryset = People.objects.all()
        serializer_class = PeopleSerializer        






''' Below Codes Are People API Using GenericAPIView and Model Mixin Classes '''

''' 
GenericAPIView inherits the APIView. 
HTTP request action methods are defined in respected ModelMixin classes. 
ModelMixin classes also returns the status code, and serialized data as the body of the response. 
'''

'''
The ListModelMixin and CreateModelMixin classes does not require any PK 

The RetrieveModelMixin, UpdateModelMixin, and DestroyModelMixin needed a PK to perform an operation. 
So, we can create two classes and inherit those model mixins, and implement the respected HTTP methods. 
'''

''' Group Implementation of the ModelMixin Classes (if PK is needed or not) '''

# class GetCreatePeopleAPI(GenericAPIView, ListModelMixin, CreateModelMixin): 
#         queryset = People.objects.all()
#         serializer_class = PeopleSerializer
        
#         # ListModelMixin
#         def get(self, request, *args, **kwargs): 
#                 return self.list(request, *args, **kwargs)
        
        
#         # CreateModelMixin
#         def post(self, request, *args, **kwargs): 
#                 return self.create(request, *args, **kwargs)
        

# class RetriveUpdateDeletePeopleAPI(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin): 
#         queryset = People.objects.all()
#         serializer_class = PeopleSerializer
        
        
#         # RetrieveModelMixin
#         def get(self, request, *args, **kwargs): 
#                 return self.retrieve(request, *args, **kwargs)
        
#         # UpdateModelMixin
#         def put(self, request, *args, **kwargs): 
#                 return self.update(request, *args, **kwargs)
        
#         # DestroyModelMixin 
#         def delete(self, request, *args, **kwargs): 
#                 return self.destroy(request, *args, **kwargs)



''' Individual Implementation of all the ModelMixin Classes '''


# # TO GET ALL THE MODEL DATA (GET)  (PK NOT NEEDED)
# class GetAllPeopleAPI(GenericAPIView, ListModelMixin): 
        
#         # This queryset and serializer_class is part of the GenericAPIView class
#         queryset = People.objects.all()
#         serializer_class = PeopleSerializer
        
#         # ListModelMixin class is for returning all the data, so a get method is needed to implement. 
        
#         # the ListModelMixin class has list method, so call this method and it will return all the data along with status code 
#         def get(self, request, *args, **kwargs): 
#                 return self.list(request, *args, **kwargs)
        

# # TO CREATE AN OBJECT IN THE DATABASE (POST) (PK NOT NEEDED)
# class CreatePeopleAPI(GenericAPIView, CreateModelMixin): 
#         queryset = People.objects.all()
#         serializer_class = PeopleSerializer
        
#         # CreateModelMixin class is responsible to create a model instance in the database. 
        
        
#         # call the create method which is implemented inside the CreateModelMixin class, it will handle all the necesary work for creating, validating an object 
#         # and returning the newly created object. 
#         def post(self, request, *args, **kwargs): 
#                 return self.create(request, *args, **kwargs)
        

        
# # TO GET A SINGLE MODEL OBJECT (GET) (PK NEEDED)
# class RetrivePeopleAPI(GenericAPIView, RetrieveModelMixin): 
#         queryset = People.objects.all()
#         serializer_class = PeopleSerializer
        
#         # RerriveModelMixin class is responsible to return a single model object from the database. 
#         # lookup_field = 'id'  # the default is pk, but we can change with lookup_field attribute 
        
#         # Call the retirieve method that is implemented inside the RetriveModelMixin class. 
#         # This will allow to return a single model object data. Pk is needed. GET request. 
#         def get(self, request, *args, **kwargs): 
#                 return self.retrieve(request, *args, **kwargs)
        

# # TO UPDATE A MODEL OBJECT. CAN HANDLE BOTH : PUT + PATCH. PK IS NEEDED. METHOD IS => PUT 
# class UpdatePeopleAPI(GenericAPIView, UpdateModelMixin): 
#         queryset = People.objects.all()
#         serializer_class = PeopleSerializer
        
#         # UpdateModelMixin class is responsible to update a model instance. It can handle both update request : put and patch 

        
#         # Call the update method that is implemented inside the UpdateModelMixin class. 
#         # as this is an update task, the method is put. 
#         def put(self, request, *args, **kwargs): 
#                 return self.update(request, *args, **kwargs)
        

# # TO DELETE A MODEL OBJECT (DATA). PK IS NEEDED. METHOD IS - DELETE. 
# class DestroyPeopleAPI(GenericAPIView, DestroyModelMixin): 
#         queryset = People.objects.all()
#         serializer_class = PeopleSerializer
        
#         # DestroyModelMixin is responsible for deleting a model instance from the database. The method is delete. 

        
#         # Implement the delete HTTP method, and inside the delete method, 
#         # call the destroy method, which is implemented inside the DestroyModelMixin class. It will delete the model object. 
#         def delete(self, request, *args, **kwargs): 
#                 return self.destroy(request, *args, **kwargs)















''' Below Code Is PoepleAPI Using APIView  '''

# class PeopleAPI(APIView): 
#         def get(self, request, id=None, fotmat=None): 
#                 if id is not None: 
#                         try : 
#                                 people = People.objects.get(id=id)
#                                 serializer = PeopleSerializer(people)
#                                 return Response(serializer.data, status=status.HTTP_200_OK)
#                         except ObjectDoesNotExist: 
#                                 return Response({'msg' : 'The ID Does Not Exist !!'}, status=status.HTTP_400_BAD_REQUEST)
                
#                 peoples = People.objects.all()
#                 serializer = PeopleSerializer(peoples, many=True)
#                 return Response(serializer.data, status=status.HTTP_200_OK)
        
#         def post(self, request, format=None): 
#                 data = request.data 
#                 serializer = PeopleSerializer(data=data)
#                 if serializer.is_valid(): 
#                         serializer.save()
#                         return Response({'msg' : 'Data Created Successfully !!', 'data' : serializer.data}, status=status.HTTP_201_CREATED)
#                 return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#         def put(self, request, id=None, format=None): 
#                 if id : 
#                         try : 
#                                 data = request.data 
#                                 people = People.objects.get(id=id)
#                                 serializer = PeopleSerializer(people, data=data)
#                                 if serializer.is_valid(): 
#                                         serializer.save()
#                                         return Response({'msg' : 'Complete Data Updated Is Successfull !!', 'data' : serializer.data}, status=status.HTTP_200_OK)
#                                 return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#                         except ObjectDoesNotExist: 
#                                 return Response({'msg' : 'The ID Does Not Exist !!'}, status=status.HTTP_400_BAD_REQUEST)
#                 return Response({'msg' : 'ID Must Be Provided To Complete Update Data !!'}, status=status.HTTP_400_BAD_REQUEST)
                
#         def patch(self, request, id=None, format=None): 
#                 if id : 
#                         try : 
#                                 data = request.data 
#                                 people = People.objects.get(id=id)
#                                 serializer = PeopleSerializer(people, data=data, partial=True)
#                                 if serializer.is_valid(): 
#                                         serializer.save()
#                                         return Response({'msg' : 'Partial Data Update Is Successfull !!', 'data' : serializer.data}, status=status.HTTP_200_OK)
#                                 return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#                         except ObjectDoesNotExist: 
#                                 return Response({'msg' : 'The ID Does Not Exist !!'}, status=status.HTTP_400_BAD_REQUEST)
#                 return Response({'msg' : 'ID Must Be Provided To Partially Update Data !!'}, status=status.HTTP_400_BAD_REQUEST)
                        
#         def delete(self, request, id=None, format=None): 
#                 if id : 
#                         try: 
#                                 people = People.objects.get(id=id)
#                                 name = people.name 
#                                 people.delete()
#                                 return Response({'msg' : f"{name}'s Data Is Successfully Deleted !!"}, status=status.HTTP_200_OK)
#                         except ObjectDoesNotExist: 
#                                 return Response({'msg' : 'The ID Does Not Exist !!'}, status=status.HTTP_400_BAD_REQUEST)
                        
#                 return Response({'msg' : 'ID Must Be Provided To Delete Data !!'}, status=status.HTTP_400_BAD_REQUEST)
        
        
        
''' Below Is The Same API Using api_view Decorator '''

# @api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
# def people_api(request, id=None): 

#         # id = request.data.get('id', None) | if client app is used, get the id from the request.data (this is parsed_data)
        
#         if request.method == 'GET':     
#                 if id is not None: 
#                         try : 
#                                 people = People.objects.get(id=id)
#                                 serializer = PeopleSerializer(people)
#                                 return Response(serializer.data, status=status.HTTP_200_OK)
#                         except ObjectDoesNotExist : 
#                                 return Response({'msg' : 'The data does not exist !!'}, status=status.HTTP_400_BAD_REQUEST)
                
#                 peoples = People.objects.all()
#                 serializer = PeopleSerializer(peoples, many=True)
#                 return Response(serializer.data, status=status.HTTP_200_OK)


#         if request.method == 'POST': 
#                 data = request.data 
#                 serializer = PeopleSerializer(data=data)
#                 if serializer.is_valid(): 
#                         serializer.save()
#                         return Response({'msg' : 'Data Created Successfully !!', 'data' : serializer.data}, status=status.HTTP_201_CREATED)
#                 return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#         if request.method == 'PUT': 
#                 if id is not None: 
#                         try : 
#                                 people = People.objects.get(id=id)
#                                 serializer = PeopleSerializer(people, data=request.data )
#                                 if serializer.is_valid(): 
#                                         serializer.save()
#                                         return Response({'msg' : 'Data successfulll updated !!', 'data' : serializer.data}, status=status.HTTP_200_OK)
#                                 # if there are any errors 
#                                 return Response({serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
#                         except ObjectDoesNotExist: 
#                                 return Response({'msg' : 'The data does not exist !!'}, status=status.HTTP_400_BAD_REQUEST)
#                 # if the id is not provided 
#                 return Response({'msg' : 'ID must be provided to update data'}, status=status.HTTP_400_BAD_REQUEST)
        
#         if request.method == 'PATCH': 
#                 if id is not None:
#                         try : 
#                                 people = People.objects.get(id=id)
#                                 serializer = PeopleSerializer(people, data=request.data, partial=True)
#                                 if serializer.is_valid(): 
#                                         serializer.save()
#                                         return Response({'msg' : 'Data successfulll updated !!', 'data' : serializer.data}, status=status.HTTP_200_OK)
#                                 # if there are any errors 
#                                 return Response({serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
#                         except ObjectDoesNotExist: 
#                                 return Response({'msg' : 'The data does not exist !!'}, status=status.HTTP_400_BAD_REQUEST)
#                 # if the id is not provided 
#                 return Response({'msg' : 'ID must be provided to update data'}, status=status.HTTP_400_BAD_REQUEST)

#         if request.method == 'DELETE': 
#                 if id is not None: 
#                         try : 
#                                 people = People.objects.get(id=id)
#                                 people.delete()
#                                 return Response({'msg' : 'Data successfulll deleted !!'}, status=status.HTTP_200_OK)
#                         except ObjectDoesNotExist: 
#                                 return Response({'msg' : 'The data does not exist !!'}, status=status.HTTP_400_BAD_REQUEST)
#                 # if the id is not provided 
#                 return Response({'msg' : 'ID must be provided to delete data'}, status=status.HTTP_400_BAD_REQUEST)
        
                
