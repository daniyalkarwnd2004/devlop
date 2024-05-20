def number(a, b):
    count = 0
    for i in range(a):
        count += b
    return count


a = int(input("number : "))
b = int(input("number : "))
print(number(a, b))
