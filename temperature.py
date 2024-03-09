# Temperature conversion program

from functools import wraps

# We use functools to send the copied version of the cellservice function to the decorator
def dec(func):
    # Create a decorator to perform the temperature calculation
    @wraps(func)
    def inner(text, temp):

        # Create a condition for performing calculation tasks
        if text == "c".lower():
            f = temp * 1.8 + 32
            print(f"Temperature from Celsius to Fahrenheit {f}")
            k = temp + 273.15
            print(f"Temperature from Celsius to Kelvin {k}")
        elif text == "f".lower():
            c = (temp - 32) / 1.8
            print(f"Temperature from Fahrenheit to Celsius{c}")
            k = (temp + 459.67) / 1.8
            print(f"Temperature from Fahrenheit to Kelvin {k}")
        elif text == "k".lower():
            c = temp - 273.15
            print(f"Temperature from Kelvin to Celsius {c}")
            f = temp * 1.8 - 459.67
            print(f"Temperature from Kelvin to Fahrenheit {f}")
        else:
            print("Error Please enter correct information :(")
            func(text, temp)
    return inner


@dec
def celsius(text1, temperature1):
    # We receive entries
    print(text1, temperature1)


temperature = int(input("Please enter the temperature value: "))
textinput = input("Please enter the temperature type : ")

celsius(textinput, temperature)
