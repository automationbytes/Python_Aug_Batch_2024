import requests
import json
from myObj import myObj

print(myObj)
req = requests.put("https://webservice.toscacloud.com/api/v1/Employee",json=myObj)
print(req.status_code)
print(json.dumps(req.json(), indent=4))