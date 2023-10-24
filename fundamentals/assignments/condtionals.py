# Q1. Write a website simulator that allows users to signup and signin.
#     Conditions for signup:
#           - Name
#           - Email(unique)
#           - Phone(unique)
#           - Password(atleast 5 characters)
#     Conditions for signin:
#           - Must have signed up already
#           - Email must be correct - case insensitive
#           - Password must be correct
# NOTE: At each stage notify the user witht the proper message

# CORRECTION

print("Welcome to our Awesome, what do you want to do?")
print("""
1. Signin
2. Signup""")

database = {
    "name": "Omale David",
    "email": "omale@yahoo.com",
    "phone": "08039014190",
    "password": "password"
}

option = input(": ")

if option.strip() == "1":
    email = input("Please enter your email: ")
    password = input("Please enter your password: ")
    if email == database.get('email'):
        if password == database.get('password'):
            print("Hi {}, welcome back to our Awesome website!".format(database.get('name')))
        else:
            print("Invalid password!")
    else:
        print("Invalid email")
elif option.strip() == "2":
    name = input("Tell us your name: ")
    if name:
        email = input("Tell us your email: ")
        if email and ("@" in email) and ("." in email):
            phone = input("Whats your phone number: ")
            if phone and phone.startswith("0") and len(phone) == 11 and phone.isdigit():
                password = input("Choose a password (8 characters): ")
                if password and len(password) >= 8:
                    database['name'] = name
                    database['email'] = email
                    database['phone'] = phone
                    database['password'] = password
                    print("Great! Now you can login.")
                else:
                    print("Password must be atleast 8 characters!")
            else:
                print("Invalid phone number or phone number not provided!")
        else:
            print("Invalid email or email not provided!")
    else:
        print("Name is required!")
else:
    print("Please choose a valid option")