def number(a, b, c):
    p = (a + b + c) / 2
    s = (p*(p - a) * (p - b) * (p - c)) ** 0.5
    return s


a = float(input("a : "))
b = float(input("b : "))
c = float(input("c : "))
print(number(a, b, c))