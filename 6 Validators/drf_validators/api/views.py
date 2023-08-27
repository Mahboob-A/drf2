from functools import partial
from django.shortcuts import render
from io import BytesIO
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.core.exceptions import ObjectDoesNotExist
from django.views import View

from .serializer import StudentSerializer
from .models import Student



@method_decorator(csrf_exempt, name='dispatch')
class StudentAPI(View): 
        def get(self, request, *args, **kwargs): 
                json_data = request.body 
                stream = BytesIO(json_data)
                parsed_data = JSONParser().parse(stream) # pythonic data 
                roll = parsed_data.get('roll', None)
        
                # If id is passed, then return only single student data 
                if roll is not None: 
                        # serialization : complex to json 
                        single_student_data = Student.objects.get(roll=roll)
                        serializer = StudentSerializer(single_student_data)
                        json_data = JSONRenderer().render(serializer.data)
                        return HttpResponse(json_data, content_type='application/json')

                # if id is not passed, then return all student data 
                all_student_data = Student.objects.all()
                serializer = StudentSerializer(all_student_data, many=True)
                json_data = JSONRenderer().render(serializer.data)
                return HttpResponse(json_data, content_type='application/json')
        
        def post(self, request, *args, **kwargs):  
                json_data = request.body
                # make the json data into stream data 
                stream = BytesIO(json_data)
                # convert the stream data into pythonic data 
                parsed_data = JSONParser().parse(stream)
                # convert the pythonic data into compelx data by serializing it 
                # here, while serializing the python data, we have to pass it as data=python data(parsed_data). else, 500 internal server error occure 
                roll = parsed_data.get('roll')
                
                # if an object with the roll is already exists, then can't create new object as roll is unique 
                try: 
                        single_student_data = Student.objects.get(roll=roll)
                        response_data = {
                                'msg' : 'Roll already exists'
                        }
                        json_data = JSONRenderer().render(response_data)
                        return HttpResponse(json_data, content_type='application/json')
                
                # create only if the object is already created using the roll 
                except ObjectDoesNotExist:
                        serializer = StudentSerializer(data=parsed_data)
                        # save the data 
                        if serializer.is_valid(): 
                                serializer.save()
                                response_data = {
                                        'msg' : 'Data Created Successfully!'
                                }
                                json_data = JSONRenderer().render(response_data)
                                return HttpResponse(json_data, content_type='application/json')
                        
                        #  if there are any erros, and object is not created for any validation failures, 
                        # then response with the errors
                        json_data = JSONRenderer().render(serializer.errors)
                        return HttpResponse(json_data, content_type='application/json')
                
        
        def put(self, request, *args, **kwargs): 
                json_data = request.body
                # convert into stream data 
                stream = BytesIO(json_data)
                # convert into pythonic data 
                parsed_data = JSONParser().parse(stream) # as the parsed data is a pythonic dict. 
                roll = parsed_data.get('roll')  # roll will be passed, as I am updating the object using roll, since passing roll is mandadory 
                
                # get the student model object using the roll 
                single_student_data = Student.objects.get(roll=roll)
                
                # now, it is the time to update the data. we have to  serialize based on the decision whether we want to update all the data or, partial data  
                # pass the single_student_object and the data=pythonic data to proceed with Complete update the model object. 
                # howover, to make a partial update, also pass partial=True along with the those data 
                
                # Complete Update ( need all the data to be passed)
                # serializer = StudentSerializer(single_student_data, data=parsed_data)
                # Partial Update 
                serializer = StudentSerializer(single_student_data, data=parsed_data, partial=True)
                
                # save the serializer calling is_valid 
                if serializer.is_valid(): 
                        serializer.save()
                        response_data = {
                                'msg' : 'Data Updated Successfully !!'
                        }
                        json_data = JSONRenderer().render(response_data)
                        return HttpResponse(json_data, content_type='application/json')
                
                # returns errors if any error is occured 
                json_data = JSONRenderer().render(serializer.errors) 
                return HttpResponse(json_data, content_type='application/json')

        
        def delete(self, request, *args, **kwargs): 
                json_data = request.body 
                
                # convert into stream data 
                stream = BytesIO(json_data)
                
                # convert into pythonic data 
                parsed_data = JSONParser().parse(stream)
                
                # get the roll of the student 
                roll = parsed_data.get('roll')
                
                # delete the model object from the database using the roll 
                try: 
                        Student.objects.get(roll=roll).delete()
                        # send response 
                        response_data = {
                                'msg' : 'Data Deleted Successfully !!'
                        }
                        # convert the pythonic data into json data 
                        json_data = JSONRenderer().render(response_data)
                        return HttpResponse(json_data, content_type='application/json')
                
                except Exception: 
                        # If the data is already deleted, then send an unsuccessful message 
                        response_data = { 
                                'error' : f'Student with roll {roll} is not found !! It might be alread deleted or it is an invalid roll !!'
                        }
                        # convert the pythonic data into json data 
                        # json_data = JSONRenderer().render(response_data)
                        # return HttpResponse(json_data, content_type='application/json')
                        
                        # we can also use JsonResponse. It is the combination of 
                        # JSONRenderer and returning HttpRenponse 
                        return JsonResponse(response_data, safe=False)                





'''
Function Based: 

# GET api 
@csrf_exempt
def student_api(request): 
        # GET REQUEST 
        if request.method == 'GET': 
                # deserialization : json to complex 
                json_data = request.body 
                stream = BytesIO(json_data)
                parsed_data = JSONParser().parse(stream) # pythonic data 
                roll = parsed_data.get('roll', None)
                
                # If id is passed, then return only single student data 
                if roll is not None: 
                        # serialization : complex to json 
                        single_student_data = Student.objects.get(roll=roll)
                        serializer = StudentSerializer(single_student_data)
                        json_data = JSONRenderer().render(serializer.data)
                        return HttpResponse(json_data, content_type='application/json')

                # if id is not passed, then return all student data 
                all_student_data = Student.objects.all()
                serializer = StudentSerializer(all_student_data, many=True)
                json_data = JSONRenderer().render(serializer.data)
                return HttpResponse(json_data, content_type='application/json')
        
        # POST REQUEST 
        if request.method == 'POST': 
                # csrf is needed for post operatio. exempt it in testing cases 
                # Deserialize : get the json data 
                json_data = request.body
                # make the json data into stream data 
                stream = BytesIO(json_data)
                # convert the stream data into pythonic data 
                parsed_data = JSONParser().parse(stream)
                # convert the pythonic data into compelx data by serializing it 
                # here, while serializing the python data, we have to pass it as data=python data(parsed_data). else, 500 internal server error occure 
                serializer = StudentSerializer(data=parsed_data)
                
                # save the data 
                if serializer.is_valid(): 
                        serializer.save()
                        response_data = {
                                'msg' : 'Data Created Successfully!'
                        }
                        json_data = JSONRenderer().render(response_data)
                        return HttpResponse(json_data, content_type='application/json')
                
                #  if there are any erros, response with the errors
                json_data = JSONRenderer().render(serializer.errors)
                return HttpResponse(json_data, content_type='application/json')
        
        # PUT REQUEST (update)
        if request.method == 'PUT': 
                # print(request.body)  # the json data 
                # get the json data 
                json_data = request.body
                # convert into stream data 
                stream = BytesIO(json_data)
                # convert into pythonic data 
                parsed_data = JSONParser().parse(stream) # as the parsed data is a pythonic dict. 
                roll = parsed_data.get('roll')  # roll will be passed, as I am updating the object using roll, since passing roll is mandadory 
                
                # get the student model object using the roll 
                single_student_data = Student.objects.get(roll=roll)
                
                # now, it is the time to update the data. we have to  serialize based on the decision whether we want to update all the data or, partial data  
                # pass the single_student_object and the data=pythonic data to proceed with Complete update the model object. 
                # howover, to make a partial update, also pass partial=True along with the those data 
                
                # Complete Update ( need all the data to be passed)
                # serializer = StudentSerializer(single_student_data, data=parsed_data)
                # Partial Update 
                serializer = StudentSerializer(single_student_data, data=parsed_data, partial=True)
                
                # save the serializer calling is_valid 
                if serializer.is_valid(): 
                        serializer.save()
                        response_data = {
                                'msg' : 'Data Updated Successfully !!'
                        }
                        json_data = JSONRenderer().render(response_data)
                        return HttpResponse(json_data, content_type='application/json')
                
                # returns errors if any error is occured 
                json_data = JSONRenderer().render(serializer.errors) 
                return HttpResponse(json_data, content_type='application/json')
                
        # DELETE Request (delete)
        if request.method == 'DELETE': 
                # Deserialization 
                # get the json data from rquest body 
                json_data = request.body 
                
                # convert into stream data 
                stream = BytesIO(json_data)
                
                # convert into pythonic data 
                parsed_data = JSONParser().parse(stream)
                
                # get the roll of the student 
                roll = parsed_data.get('roll')
                
                # delete the model object from the database using the roll 
                try: 
                        Student.objects.get(roll=roll).delete()
                        # send response 
                        response_data = {
                                'msg' : 'Data Deleted Successfully !!'
                        }
                        # convert the pythonic data into json data 
                        json_data = JSONRenderer().render(response_data)
                        return HttpResponse(json_data, content_type='application/json')
                
                except Exception: 
                        # If the data is already deleted, then send an unsuccessful message 
                        response_data = { 
                                'error' : f'Student with roll {roll} is not found !! It might be alread deleted or it is an invalid roll !!'
                        }
                        # convert the pythonic data into json data 
                        # json_data = JSONRenderer().render(response_data)
                        # return HttpResponse(json_data, content_type='application/json')
                        
                        # we can also use JsonResponse. It is the combination of 
                        # JSONRenderer and returning HttpRenponse 
                        return JsonResponse(response_data, safe=False)
        

'''

                
                        