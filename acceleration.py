def number(a, b, c):
    m = (a - b) * 60 / c
    return m


a = int(input("number : "))
b = int(input("number : "))
c = int(input("number : "))
print(number(a, b, c))