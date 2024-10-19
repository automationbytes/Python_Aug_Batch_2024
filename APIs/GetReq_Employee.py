import requests
import json


req = requests.get("https://webservice.toscacloud.com/api/v1/Shops")
print(req.status_code)
print(req.text)
print(req.json())
print(json.dumps(req.json(),indent=4))
