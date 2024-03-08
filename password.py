import random
import string

lowe_case = string.ascii_lowercase
upper_case = string.ascii_uppercase
number = "0123456789"
symbol = "~!@#$%^&*(){}"
password_all = lowe_case + upper_case + number + symbol

while True:
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
