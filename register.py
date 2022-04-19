import re
import ast
email_regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
phone_regex = re.compile(r'^01[0125][0-9]{8}$')


def register_form():
    print("please enter your information correctly")
    first_name = input("First name : ")
    while not first_name.isalpha():
        print("sorry enter valid name")
        first_name = input("First name : ")

    last_name = input("Last name : ")
    while not last_name.isalpha():
        print("sorry enter valid name")
        last_name = input("Last name : ")

    email = input("Email : ")
    while not re.fullmatch(email_regex, email):
        print("sorry enter valid email")
        email = input("Email : ")
    user_data = open("user-data.txt", "r")
    lines = user_data.readlines()
    for line in lines:
        user = ast.literal_eval(line)
        if email == user["email"]:
            print("sorry this email exists enter another email")
            email = input("Email : ")

    password = input("Password : ")
    while not password.isalnum():
        print("sorry enter valid password")
        password = input("Password : ")

    confirm_password = input("Confirm password : ")
    while confirm_password != password:
        print("please enter the same password")
        confirm_password = input("Confirm password : ")

    mobile = input("Mobile phone : ")
    while not re.fullmatch(phone_regex, mobile):
        print("please enter valid egyptian number")
        mobile = input("Mobile phone : ")

    user_data = {
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'password': password,
        'mobile': mobile
    }
    return user_data
