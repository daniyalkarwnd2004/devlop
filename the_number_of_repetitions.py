def number(name):
    list_number = []
    for i in name:
        list_number.append(i)
    return max(list_number, key=list_number.count)


name = input("name : ").split(" ")
print(number(name))
