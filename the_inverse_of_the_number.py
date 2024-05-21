number = int(input("number : "))
revers_num = 0
while number > 0:
    temp = number % 10
    revers_num = revers_num * 10 + temp
    number = number // 10
    x = revers_num * 2
    print(x)
