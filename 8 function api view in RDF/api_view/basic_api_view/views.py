from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response


# api_view takes GET request by default. 
# if we want to add more request, then add a list in the decorator and add the requests we want to allow in the API. 
# To know more about the api_view, head on to my note on notion here : https://www.notion.so/Video-08-Function-Based-API-View-in-Django-REST-Framework-e5157be17aed48b89cb37d6a1c039896?pvs=4

'''request.data'''
# By request.data, we will directly get the parsed_pythonic_data 
# Here, no need to get json_data using request.body and then parse it. 

'''Response'''
# By using Response, we need to pass pythonic data in it, and it will handle rendering to correnponding data type to pass to the client. 
# Here no need to pass content_type 


'''Examples'''
# simple GET 

# @api_view()
# def simple_api(request): 
#         return Response({'msg' : 'Hello This is a simple API !'})   

# both are equavalent. GET method is default in the api_view. 

# @api_view(['GET'])
# def simple_api(request): 
#         return Response({'msg' : 'Hello This is a simple API !'})   

# but using other than GET, we need pass a list of the mehods we want to use 
# now without specifying GET, GET will not work as we have passed a list but not defined the GET 
# @api_view(['POST'])
# def simple_api(request): 
#         print(request.data)
#         return Response({'msg' : 'Hello This is a simple API POST Request !', 'data' : request.data})   


@api_view(['GET', 'POST'])
def simple_api(request): 
        
        if request.method == 'GET': 
                return Response({'msg' : 'This is a simple GET Request !! '})
        
        if request.method == 'POST': 
                print(request.data)
                return Response({'msg' : 'Hello This is a simple API POST Request !', 'data' : request.data})   