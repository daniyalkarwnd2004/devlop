def func_name(name):
    list_name = []
    for i in name:
        list_name.append((len(i), i))
    print(max(list_name))


name = input("text : ").split(' ')
func_name(name)
