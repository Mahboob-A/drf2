
import requests 
import json

# making post request using our api to store the data in the server 

URL = ' http://127.0.0.1:8000/stdata/'

data = {
        'name' : 'Abir Auan', 
        'roll' : 103, 
        'city' : 'Rnj'
}

# convert the data into json 
json_data = json.dumps(data)

resp = requests.post(url=URL, data=json_data)

data = resp.json()

print(data)