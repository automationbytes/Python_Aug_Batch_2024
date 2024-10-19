import requests
import json

myObj = {
  "city": "Chennai",
  "country": "India",
  "name": "DevLabs"
}

req = requests.post("https://webservice.toscacloud.com/api/v1/Shops",json=myObj)
print(req.status_code)

print(json.dumps(req.json(),indent=4))

getReq = requests.get("https://webservice.toscacloud.com/api/v1/Shops")
print(getReq.status_code)

print(json.dumps(getReq.json(),indent=4))

