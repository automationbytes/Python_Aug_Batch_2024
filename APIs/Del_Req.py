import requests
import json


req = requests.delete("https://webservice.toscacloud.com/api/v1/Shops/3")
print(req.status_code)

print("****************")

req = requests.get("https://webservice.toscacloud.com/api/v1/Shops")
print(req.status_code)
print(req.text)
print(req.json())
print(json.dumps(req.json(),indent=4))
