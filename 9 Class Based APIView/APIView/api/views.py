

from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.core.exceptions import ObjectDoesNotExist
from .models import People
from .serializer import PeopleSerializer




class PeopleAPI(APIView): 
        def get(self, request, id=None, fotmat=None): 
                if id is not None: 
                        try : 
                                people = People.objects.get(id=id)
                                serializer = PeopleSerializer(people)
                                return Response(serializer.data, status=status.HTTP_200_OK)
                        except ObjectDoesNotExist: 
                                return Response({'msg' : 'The ID Does Not Exist !!'}, status=status.HTTP_400_BAD_REQUEST)
                
                peoples = People.objects.all()
                serializer = PeopleSerializer(peoples, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
        
        def post(self, request, format=None): 
                data = request.data 
                serializer = PeopleSerializer(data=data)
                if serializer.is_valid(): 
                        serializer.save()
                        return Response({'msg' : 'Data Created Successfully !!', 'data' : serializer.data}, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        def put(self, request, id=None, format=None): 
                if id : 
                        try : 
                                data = request.data 
                                people = People.objects.get(id=id)
                                serializer = PeopleSerializer(people, data=data)
                                if serializer.is_valid(): 
                                        serializer.save()
                                        return Response({'msg' : 'Complete Data Updated Is Successfull !!', 'data' : serializer.data}, status=status.HTTP_200_OK)
                                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                        except ObjectDoesNotExist: 
                                return Response({'msg' : 'The ID Does Not Exist !!'}, status=status.HTTP_400_BAD_REQUEST)
                return Response({'msg' : 'ID Must Be Provided To Complete Update Data !!'}, status=status.HTTP_400_BAD_REQUEST)
                
        def patch(self, request, id=None, format=None): 
                if id : 
                        try : 
                                data = request.data 
                                people = People.objects.get(id=id)
                                serializer = PeopleSerializer(people, data=data, partial=True)
                                if serializer.is_valid(): 
                                        serializer.save()
                                        return Response({'msg' : 'Partial Data Update Is Successfull !!', 'data' : serializer.data}, status=status.HTTP_200_OK)
                                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                        except ObjectDoesNotExist: 
                                return Response({'msg' : 'The ID Does Not Exist !!'}, status=status.HTTP_400_BAD_REQUEST)
                return Response({'msg' : 'ID Must Be Provided To Partially Update Data !!'}, status=status.HTTP_400_BAD_REQUEST)
                        
        def delete(self, request, id=None, format=None): 
                if id : 
                        try: 
                                people = People.objects.get(id=id)
                                name = people.name 
                                people.delete()
                                return Response({'msg' : f"{name}'s Data Is Successfully Deleted !!"}, status=status.HTTP_200_OK)
                        except ObjectDoesNotExist: 
                                return Response({'msg' : 'The ID Does Not Exist !!'}, status=status.HTTP_400_BAD_REQUEST)
                        
                return Response({'msg' : 'ID Must Be Provided To Delete Data !!'}, status=status.HTTP_400_BAD_REQUEST)
        
        
        
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
        
                
