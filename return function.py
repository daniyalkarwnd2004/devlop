def number(digit):
    if digit == 0:
        return 1
    if digit % 10 < 5:
        return number(digit // 10)
    else:
        return digit % 10 * number(digit // 10)


print(number(5843265124328))
