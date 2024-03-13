import datetime

# This function takes the age from the user, calculates it with today's date,
# and tells you the year of your birth in the Gregorian calendar


def date_birth(birth):
    date = datetime.datetime.now()
    year = int(date.year)
    Date_of_birth = year - birth
    print("your year of birth : ", Date_of_birth)


# It takes the age from the user and sends it to the function
Date_Birth = int(input("Enter your age : "))
date_birth(Date_Birth)
