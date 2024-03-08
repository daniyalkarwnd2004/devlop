# add random

import random
import string

# add lowercase and uppercase and number

lowe_case = string.ascii_lowercase
upper_case = string.ascii_uppercase
number = "0123456789"
symbol = "~!@#$%^&*(){}"
password_all = lowe_case + upper_case + number + symbol


# I created a loop and displayed the items for the user to select

while True:

# Create a condition and get a number from the user for the number of digits of the code
    
    print("please select : \n1)create a password\n2)exit")
    select = input("please select : ")
    if select == "1":
        digit = int(input("please your number : "))
        password = "".join(random.sample(password_all, digit))
        print(password)
    elif select == "2":
        print("Good")
        break
    else:
        print("please your select :) ")
