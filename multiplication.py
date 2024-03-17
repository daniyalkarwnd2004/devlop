# We take the number from the user and multiply it

def multiplication(number):
    # We define conditions

    if number == 1:
        for i in range(1, 11):
            print(f"{number} * {i} = ", number * i)
    elif number == 2:
        for i in range(1, 11):
            print(f"{number} * {i} = ", number * i)
    elif number == 3:
        for i in range(1, 11):
            print(f"{number} * {i} = ", number * i)
    elif number == 4:
        for i in range(1, 11):
            print(f"{number} * {i} = ", number * i)
    elif number == 5:
        for i in range(1, 11):
            print(f"{number} * {i} = ", number * i)
    elif number == 6:
        for i in range(1, 11):
            print(f"{number} * {i} = ", number * i)
    elif number == 7:
        for i in range(1, 11):
            print(f"{number} * {i} = ", number * i)
    elif number == 8:
        for i in range(1, 11):
            print(f"{number} * {i} = ", number * i)
    elif number == 9:
        for i in range(1, 11):
            print(f"{number} * {i} = ", number * i)
    elif number == 10:
        for i in range(1, 11):
            print(f"{number} * {i} = ", number * i)
    else:
        print("Error")


digit = int(input("number : "))
multiplication(digit)
