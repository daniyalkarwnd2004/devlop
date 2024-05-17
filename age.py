def age(a):
    second = a * 3165e4
    minute = second / 60
    hour = second / 3600
    print(second)
    print(minute)
    print(hour)


a = int(input("AGE : "))
age(a)