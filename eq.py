def number(a, b, c):
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        print("Not root")
    elif delta == 0:
        print(" x1 = x2 = ", -b / (2.0 * a))
    else:
        print(" x1 = ", (-b + delta ** 0.5) / (2.0 * a))
        print(" x2 = ", (-b - delta ** 0.5) / (2.0 * a))


a = int(input("number : "))
b = int(input("number : "))
c = int(input("number : "))
number(a, b, c)
