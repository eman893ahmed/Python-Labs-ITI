import re

def validate_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

    try:
       if not re.match(pattern, email):
           raise ("Invalid Email Format")    
    except :
        print ("Error: Invalid input")
    else:
        print("You are authorized!")
 
useremail = input("Enter your email address: ")
validate_email(useremail)