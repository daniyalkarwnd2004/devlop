def list_number(number):
    count = 0
    for i in number:
        if "0" <= i <= "9":
            count += 1
    print(count)


digit = input("number : ")
list_number(digit)

