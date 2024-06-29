from math import tan, pi


def number():
    digit = float(input("number : "))
    tol = float(input("number tol : "))
    sum1 = digit * (tol ** 2) / (4 * tan(pi / digit))
    print(sum1)


number()