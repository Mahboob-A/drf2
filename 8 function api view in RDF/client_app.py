import requests
import json

URL = 'http://127.0.0.1:8000/simple_api/'

# GET Operation 
def get_student_data(roll = None): 
        data = {}
        if roll is not None: 
                data = {'roll' : roll}
        json_data = json.dumps(data)
        resp = requests.get(url=URL, data=json_data)
        data = resp.json()
        print(data)
        
        
get_student_data()


'''To make other than GET request, we need to pass a headers that will content what type of data we are passing, while using @api_view'''
# To do this, see below. 
def post_student_data(): 
        data = {
                'name' : 'balam', 
                'roll' : 112, 
                'st_class' : 'X', 
                'address' : 'Lalgola', 
        }
        
        headers = {'content-Type' : 'application/json'}
        
        json_data = json.dumps(data)
        resp = requests.post(url=URL,  headers=headers,  data=json_data)
        data = resp.json()  
        print(resp)  
        print(data)

# post_student_data()


def put_data(): 

        data = {
                'name' : 'Halim', 
                'roll' : 111, 
                'st_class' : 'XII',
        } 
        
        json_data = json.dumps(data)
        resp = requests.put(url=URL, data=json_data)
        data = resp.json()
        print(resp)
        print(data)

# put_data()


def delete_data(): 

        data = {
                'roll' : 110423
        }
        
        json_data = json.dumps(data)
        resp = requests.delete(url=URL, data=json_data)
        data = resp.json()
        print(resp)
        print(data)
        
# delete_data()
