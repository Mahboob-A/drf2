import requests
import json

URL = 'http://127.0.0.1:8000/api/'

# GET Operation 
def get_student_data(roll = None): 
        data = {}
        # if roll is passed, then pass the roll in the data. Else, empty dict will be passed 
        if roll is not None: 
                data = {'roll' : roll}
        json_data = json.dumps(data)
        resp = requests.get(url=URL, data=json_data)
        data = resp.json()
        print(data)
        
        
# get_student_data(2)


# POST Operation 
def post_student_data(): 
        data = {
                'name' : 'New Don', 
                'roll' : 208, 
                'st_class' : 'XI', 
                'address' : 'Raghunathganj', 
        }
        
        json_data = json.dumps(data)
        resp = requests.post(url=URL, data=json_data)
        data = resp.json()  # json data that is returned 
        print(resp)  # http status code 
        print(data)
        
post_student_data()

# PUT Operation (UPDATE)
def put_data(): 
        '''
        I am updating the object using the roll as roll is an unique value in the model. 
        if all data are to be updated, then it is complete update, and if partial data is to be updated, 
        then it is partial update 
        '''
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

# DELETE Operation (delete)
def delete_data(): 
        # deleting based on roll as roll is unique in the model 

        data = {
                'roll' : 110423
        }
        
        json_data = json.dumps(data)
        resp = requests.delete(url=URL, data=json_data)
        data = resp.json()
        print(resp)
        print(data)
        
# delete_data()