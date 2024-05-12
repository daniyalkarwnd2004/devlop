def phone(phone_number):
    if len(phone_number) == 11:
        if phone_number.startswith("09"):
            if phone_number.isnumeric():
                return True
            else:
                return False
        else:
            return False
    else:
        return False


phone_number = input("Phone_Number : ")
print(phone(phone_number))
