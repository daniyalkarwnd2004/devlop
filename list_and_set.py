def list_set(number):
    list_number = []
    for i in number:
        number = int(i)
        list_number.append(number)
    set_number = set(list_number)
    print(set_number)
    print(len(set_number))


number_list = input("number : ").split(",")
list_set(number_list)

