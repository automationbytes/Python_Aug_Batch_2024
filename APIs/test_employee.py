import requests
import json
from jsonpath_ng.ext import parse
import pytest

# Test data to be reused
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

# Global variable to store the last name
stored_lastname = None


# Test function for PUT request
@pytest.mark.parametrize("myObj", [myObj])
def test_put_employee(myObj):
    global stored_lastname
    # Send PUT request to update employee
    response = requests.put("https://webservice.toscacloud.com/api/v1/Employee", json=myObj)

    # Assert that the response is successful
    assert response.status_code == 200, f"Failed PUT request: {response.status_code}"

    # Store the last name to use in the GET test
    stored_lastname = myObj["lastName"]

    print("PUT request successful")


# Test function for GET request (dependent on PUT)
def test_get_employee():
    global stored_lastname

    # Ensure that the stored_lastname is available
    assert stored_lastname is not None, "Last name not found from PUT request"

    # Send GET request to retrieve employee
    get_response = requests.get("https://webservice.toscacloud.com/api/v1/Employee")
    assert get_response.status_code == 200, f"Failed GET request: {get_response.status_code}"

    # Parse the JSON response
    jsonData = get_response.json()

    # Use jsonpath_ng to find the city based on lastName
    json_expr = parse(f"$[?(@.lastName == '{stored_lastname}')].address.city")
    city = json_expr.find(jsonData)

    # Ensure we found a match and compare the city
    assert len(city) > 0, f"No matching city found for last name: {stored_lastname}"
    expected_city = myObj["address"]["city"]
    assert city[0].value == expected_city, f"City mismatch: Expected {expected_city}, got {city[0].value}"

    print("GET request successful and city matches!")
