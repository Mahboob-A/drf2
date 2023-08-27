from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer

from .models import Student
from .serializer import StudentSerializer
# Create your views here.

# Model Object : Single Student Data 
def student_detail(request, id): 
        # Complex model data 
        st_data = Student.objects.get(pk=id)
        
        print('Complex Model Data : \n')
        print('Model object : ', st_data)
        print()
        # Converting the complex model object data into pythonic data using serializer 
        serializer = StudentSerializer(st_data)
        
        print('Serialized data : Complex model data converted into pythonic data \n')
        print('Type srializer: ', type(serializer))
        print('Type serializer.data : ', type(serializer.data))
        print('serializer.data : ', serializer.data)
        print()
        
        # Again converting the pythonic data / serialized data into json data 
        json_data = JSONRenderer().render(serializer.data)
        
        print('Serialized pythonic data converted into json data: \n')
        print('Type json data : ', type(json_data))
        print('Json data: ', json_data)
        # to return json data as httpresponse, use : content_type='application/json'
        return HttpResponse(json_data, content_type='application/json')

        #  json_data = JSONRenderer().render(serializer.data)  => here the json_data is a dict as it is a single modle object. 
        # if it is a queryset, then it would be a touple of list. 
        # return HttpResponse(json_data, content_type='application/json')  
        ### Convert this two lines into the below single line. 
        # return JsonResponse(serializer.data) 



# Converting a queryset 
def student_list(request): 
        # Complex model data 
        st_data = Student.objects.all()
        
        # print('Complex Model Data : \n')
        # print('Model object : ', st_data)
        # print()
        # Converting the complex model object data into pythonic data using serializer 
        serializer = StudentSerializer(st_data, many=True)  # while working with queryset and selializing, use many=True 
        
        # print('Serialized data : Complex model data converted into pythonic data \n')
        # print('Type srializer: ', type(serializer))
        # print('Type serializer.data : ', type(serializer.data))
        # print('serializer.data : ', serializer.data)
        # print()
        
        # Again converting the pythonic data / serialized data into json data 
        # json_data = JSONRenderer().render(serializer.data)
        
        # print('Serialized pythonic data converted into json data: \n')
        # print('Type json data : ', type(json_data))
        # print('Json data: ', json_data)
        # # to return json data as httpresponse, use : content_type='application/json'
        # return HttpResponse(json_data, content_type='application/json')  # this will return a list of dictionary 

        #  We can cut these two lines of code into a single line returning JsonResponse. 
        ### json_data = JSONRenderer().render(serializer.data)
        ### return HttpResponse(json_data, content_type='application/json') 
        return JsonResponse(serializer.data, safe=False)  
        # safe = False => when the data is (serializer.data) is a dict, then no need to use safe as by default it is True
        # But when we use a queryset, the serilzer.data is not a dict, rather touple of list. then we need to use
        # safe = False. 