def pascal(number):
    for i in range(0, number):
        for j in range(0, i + 1):
            print(binomial(i, j), " ", end=" ")
        print()


def binomial(number, digit):
    c = 1
    if (digit > number - digit):
        digit = number - digit
    for i in range(0, digit):
        c = c * (number - i)
        c = c // (i + 1)
    return c


number = 7
pascal(number)