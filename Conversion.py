class Conversion(object):
    def unit_of_measure(self):
        print("please choose: 1=(centimeters to inches) 2=(inches to centimeters) 3=(meters to feet) 4=(feet to meters)\n"
              "5=(kilometers to miles) 6=(miles to kilometers) 7=(millimeters to inches) 8=(inches to millimeters)")
        try:
            number = float(input("please enter a number: "))
            choose = input("choose: ")
            if choose == "1":
                new_number = number / 2.54
                print(f"{number} centimeters is {new_number} inches")
            elif choose == "2":
                new_number = number * 2.54
                print(f"{number} inches is {new_number} centimeters")
            elif choose == "3":
                new_number = number * 3.28084
                print(f"{number} meters is {new_number} feet")
            elif choose == "4":
                new_number = number / 3.28084
                print(f"{number} feet is {new_number} meters")
            elif choose == "5":
                new_number = number / 1.60934
                print(f"{number} kilometers is {new_number} miles")
            elif choose == "6":
                new_number = number * 1.60934
                print(f"{number} miles is {new_number} kilometers")
            elif choose == "7":
                new_number = number / 25.4
                print(f"{number} millimeters is {new_number} inches")
            elif choose == "8":
                new_number = number * 25.4
                print(f"{number} inches is {new_number} millimeters")
            else:
                print("Error: Invalid choice")
        except Exception as e:
            print(e)

    def weight_unit(self):
        print("please choose: 1=(kilogram to gram) 2=(gram to kilogram) 3=(kilogram to pound) 4=(pound to kilogram)\n"
              "5=(kilogram to ounce) 6=(ounce to kilogram) 7=(ton to kilogram) 8=(kilogram to milligram)")
        try:
            number = float(input("please enter a number: "))
            choose = input("choose: ")
            if choose == "1":
                new_number = number * 1000
                print(f"{number} kilograms is {new_number} grams")
            elif choose == "2":
                new_number = number * 0.001
                print(f"{number} grams is {new_number} kilograms")
            elif choose == "3":
                new_number = number * 2.20462
                print(f"{number} kilograms is {new_number} pounds")
            elif choose == "4":
                new_number = number * 0.453592
                print(f"{number} pounds is {new_number} kilograms")
            elif choose == "5":
                new_number = number * 35.274
                print(f"{number} kilograms is {new_number} ounces")
            elif choose == "6":
                new_number = number * 0.0283495
                print(f"{number} ounces is {new_number} kilograms")
            elif choose == "7":
                new_number = number * 1000
                print(f"{number} tons is {new_number} kilograms")
            elif choose == "8":
                new_number = number * 1000000
                print(f"{number} kilograms is {new_number} milligrams")
            else:
                print("Error: Invalid choice")
        except Exception as e:
            print(e)

    def temperature_unit(self):
        print("please choose: 1=(celsius to fahrenheit) 2=(fahrenheit to celsius) 3=(celsius to kelvin)\n"
              "4=(kelvin to celsius) 5=(fahrenheit to kelvin) 6=(kelvin to fahrenheit)")
        try:
            temperature = float(input("please enter a temperature: "))
            choose = input("choose: ")
            if choose == "1":
                new_temperature = (temperature * 9/5) + 32
                print(f"{temperature}°C is {new_temperature}°F")
            elif choose == "2":
                new_temperature = (temperature - 32) * 5 / 9
                print(f"{temperature}°F is {new_temperature}°C")
            elif choose == "3":
                new_temperature = temperature + 273.15
                print(f"{temperature}°C is {new_temperature}K")
            elif choose == "4":
                new_temperature = temperature - 273.15
                print(f"{temperature}K is {new_temperature}°C")
            elif choose == "5":
                new_temperature = (temperature - 32) * 5 / 9 + 273.15
                print(f"{temperature}°F is {new_temperature}K")
            elif choose == "6":
                new_temperature = (temperature - 273.15) * 9 / 5 + 32
                print(f"{temperature}K is {new_temperature}°F")
            else:
                print("Error: Invalid choice")
        except Exception as e:
            print(e)


# Example usage
conversion = Conversion()
conversion.temperature_unit()
