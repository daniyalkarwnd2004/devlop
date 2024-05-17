def number(digit):
    a1 = digit % 10
    temp = digit // 10
    a2 = temp % 10
    temp = temp // 10
    a3 = temp % 10
    temp = temp // 10
    a4 = temp % 10
    temp = temp // 10
    a5 = temp % 10
    temp = temp // 10
    print(a1, "\t", a2, "\t", a3, "\t", a4, "\t", a5)


digit = int(input("number  : "))
number(digit)
