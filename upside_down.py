def number(n):
    r1 = n % 10
    r2 = n // 10
    return r1 * 10 + r2


n = int(input("number : "))
print(number(n))