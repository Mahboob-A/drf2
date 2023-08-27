from django.shortcuts import render, HttpResponse
import io 
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser   # convert stream data into pythonic data  
from rest_framework.renderers import JSONRenderer  # convert pytonic data into json data 

from .models import Student
from .serializer import StudentSerializer




# api for creating student 
@csrf_exempt
def create_student(request): 
        if request.method == 'POST': 
                
                # Deserialization process 
                
                # step 01 : get the json data 
                json_data = request.body 
                print(request.body)
                print(json_data)
                
                # step 02: convert the json data into stream type data  
                stream = io.BytesIO(json_data)
                
                # step 03: convert the stream type data into native pythonic data 
                # when we need to convert the json data into complex data, we use JSONParser
                # json data -> python data 
                pythonic_data = JSONParser().parse(stream)
                
                # step 04: convert pythonic data into complex data 
                serializer = StudentSerializer(data=pythonic_data)
                
                # step 05: check if the data is valid 
                if serializer.is_valid(): 
                        serializer.save()
                        msg = {
                                'msg' : 'Data saved successfully!',
                        }
                        
                        # convert the pythonic data into json data to pass to the frontend 
                        # step 01: 
                        # when we want to convert the pyhon data into json data, we use JSONRenderer
                        # python data -> json data 
                        json_data = JSONRenderer().render(msg)
                        return HttpResponse(json_data, content_type='application/json')
                else: 
                        json_data = JSONRenderer().render(serializer.errors)
                        return HttpResponse(json_data, content_type='application/json')
                        
                
                