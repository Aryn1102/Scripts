import sys
from dbhelper import DBHelper

class Flipkart:

    def __init__(self):

        # connect to database
        self.db = DBHelper()

        self.menu()

    def menu(self):

        user_input = input("""
1. Enter 1 to register
2. Enter 2 to login
3. Anything else to leave
""")

        if user_input == '1':
            self.register()

        elif user_input == '2':
            self.login()

        else:
            sys.exit(1000)

    def login_menu(self):
        input("""
              1. Enter 1 to view profile
              2. Enter 2 to edit profile
              3. enter 3 to delete profile
              4. enter 4 to logout
              """)
        
    def register(self):
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        response=self.db.register(name, email, password)
        if response:
            print("Registration successful")
        else:
            print("registration failed")
        self.menu()

    def login(self):
        email=input("Enter your email: ")
        password=input("Enter your password: ")
        data=self.db.search(email, password)
        if len(data)==0:
            print("incorrect  email or password")
            self.login()
        else:
            print("Hello,"+data[0][1])
            self.login_menu()
obj = Flipkart()