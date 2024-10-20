class Employee:
    '''
    "address": {
    "city": "Delhi",
    "country": "India",
    "street": "123 Main Street",
    "zipCode": 98765
  },
  "id": 3,
  "firstName": "Devlabs",
  "lastName": "Automation"
    '''
    def __init__(self,firstName,lastName,id,city,country,street,zipCode ):
        self.firstName = firstName
        self.lastName = lastName
        self.id = id
        self.city = city
        self.country = country
        self.street = street
        self.zipCode = zipCode


    def dict(self):
        return {
            "address": {
                "city": self.city,
                "country": self.country,
                "street": self.street,
                "zipCode": self.zipCode
            },
            "id": self.id,
            "firstName": self.firstName,
            "lastName": self.lastName
        }



