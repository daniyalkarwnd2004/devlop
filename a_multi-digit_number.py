def num(number, digit):
    count = 0
    while number > 0:
        if number % 10 == digit:
            count += 1
        number = number // 10
    return count


a = int(input("number : "))
b = int(input("number : "))
print(num(a, b))
