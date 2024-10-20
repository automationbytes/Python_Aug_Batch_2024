import requests
import json
from jsonpath_ng import jsonpath
from jsonpath_ng.ext import parse

myObj = {
    "address": {
        "city": "Melbourne",
        "country": "Australia",
        "street": "123 Pine Street",
        "zipCode": 98979
    },
    "id": 3,
    "firstName": "Ricky",
    "lastName": "Ponting"
}
lastname = myObj["lastName"]
req = requests.put("https://webservice.toscacloud.com/api/v1/Employee", json=myObj)
print(req.status_code)
print(json.dumps(req.json(), indent=4))

getreq = requests.get("https://webservice.toscacloud.com/api/v1/Employee")
print(getreq.status_code)
print(getreq.text)
print(getreq.json())
print(json.dumps(getreq.json(), indent=4))
jsonData = json.loads(getreq.text)  #store as text file
print('$[?(@.lastName== '+lastname+'))].address.city')

json_Exp = parse('$[?(@.lastName== '+lastname+')].address.city')


city = json_Exp.find(jsonData)  #provide that stored output
print(city)
print(city[0].value)
if city[0].value == myObj["address"]["city"]:
    print("match")
else:
    print("not match")