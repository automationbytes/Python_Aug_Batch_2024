import requests

url = "https://countries.trevorblades.com/"

query = """{
  country(code:"IN") {
    name
    phone
    capital
    currency
    languages{
      code
      name
    }
  }
  continents{
    name
    code
    countries{
      name
      code
      capital
    }
  }
  language(code:"IN"){
    name
  }
}
"""

headers = {
    "Content-Type":'application/json'
}

res = requests.post(url,json={"query":query},headers=headers)
print(res.status_code)
print(res.json())
import json
print(json.dumps(res.json(),indent=4))