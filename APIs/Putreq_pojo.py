import requests
import json
from Employee import Employee

employee = Employee(firstName="Tom", lastName="Jerry", id=3,city="Kolkatta",country="India",street="123 Sub Street",zipCode=45678)
employeereq = employee.dict()

print(employeereq)


req = requests.put("https://webservice.toscacloud.com/api/v1/Employee",json=employeereq)
print(req.status_code)
print(json.dumps(req.json(), indent=4))