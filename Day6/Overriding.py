'''

Parent class


'''


class Google:
    def login(self):
        print("Login Page of Google")

    def homePage(self):
        print("Home Page of Google")

class Youtube(Google):
    def homePage(self):
        print("Home Page of Youtube")

Y = Youtube()
Y.login()
Y.homePage()