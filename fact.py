def fact(number):
    f = 1
    for i in range(1, number + 1):
        f *= i
    return f


def sum_fact(number):
    sum_ = 0
    for i in range(1, number + 1):
        sum_ += fact(i)
    return sum_


digit = int(input("number : "))
print(sum_fact(digit))
