def number(x1, x2, y1, y2):
    return ((x2 ** 2 - x1 ** 2) + (y2 ** 2 - y1 ** 2)) ** 0.5


x1 = int(input("x1 : "))
y1 = int(input("y1 : "))
x2 = int(input("x2 : "))
y2 = int(input("y2 : "))
print(number(x1, x2, y1, y2))