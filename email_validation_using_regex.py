import re

# Corrected email validation pattern
email_condition = r'^[a-z]+[._]?[a-z0-9]+@[a-z0-9]+\.[a-z]{2,3}$'

user_email = input("Enter your email: ")

if re.search(email_condition, user_email):
    print("Right Email")
else:
    print("Wrong Email")
