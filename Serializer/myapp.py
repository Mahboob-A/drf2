import requests

# This app is a demonstration how data can be fetched from api. (using the func in serializer django project) 080823, Tuesday 

URL = 'http://127.0.0.1:8000/2' # use http://127.0.0.1:8000 for all data and use : http://127.0.0.1:8000/val for exact data 

resp = requests.get(url=URL)

data = resp.json()

print(resp)
print(data)
