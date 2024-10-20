import requests
import requests_mock


mock = requests_mock.Mocker()

mock_response = {
    "status": "Success",
    "message": "Mocked Sample Response"
}

url = "https://example.com/api/v1/endpoint"
mock.get(url,json=mock_response)

#mocking service gonna start
with mock:
    response = requests.get(url)

    print(response.status_code)
    print(response.json())