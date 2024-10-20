import requests
import json
from jsonpath_ng import jsonpath
from jsonpath_ng.ext import parse


req = requests.get("https://webservice.toscacloud.com/api/v1/Employee")
print(req.status_code)
print(req.text)
print(req.json())
print(json.dumps(req.json(),indent=4))
jsonData = json.loads(req.text) #store as text file

json_Exp = parse('$[?(@.lastName == Ponting)].address.city')

city = json_Exp.find(jsonData) #provide that stored output
print(city)
print(city[0].value)
