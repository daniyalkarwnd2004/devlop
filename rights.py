def dec(func):
    def inner(hour):
        if hour == 140:
            rights = hour * 30000
            print(f"your rights : {rights}")

        elif hour > 190:
            print("No rights")

        elif hour > 140:
            overtime = 50000
            c = hour - 140
            additional_salary = c * overtime
            your_rights = additional_salary + (140 * 30000)
            print(f"your rights : {your_rights}")

    return inner


@dec
def rights(hour):
    print(hour * 30000)


number = int(input("hour : "))
rights(number)


