import calendar
# We call the calendar


def dec(func):

    # We use decorators to check whether the month and day are correct

    def inner(func_month, func_day):

        # We use conditions to check the correctness or incorrectness of the day and month
        if func_month > 12:
            print("please your month :)")
        elif func_day > 31:
            print("please your day :)")
        else:
            func(func_month, func_day)
    return inner

# We send the func_calendar function as an argument to the decorator

@dec
def func_calendar(month1, day1):
    print(calendar.month(day1, month1))

# We receive the day and month from the user and send it to the func_calendar function


month = int(input("month : "))
day = int(input("day : "))
func_calendar(month, day)

