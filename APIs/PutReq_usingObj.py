import requests
import json


with open('Profile.json','r') as f:
    myobj = json.load(f)

print(myobj)
req = requests.put("https://webservice.toscacloud.com/api/v1/Employee",json=myobj)
print(req.status_code)
print(json.dumps(req.json(), indent=4))