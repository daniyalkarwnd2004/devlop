def phonebook():
    dict = {}

    # I define an infinite loop that the program continues as long as the user wants
    while True:
        print("1: add\n2: search\n3: delete\n4: exit")
        select = input("select : ")

        # In this section, we receive the names of the contacts from the input and add them to our dictionary
        if select == "1":
                name = input("name : ")
                phone = int(input("number phone : "))
                dict.update({name: phone})

        # In this section, we get the user's name and display its number by searching the dictionary
        elif select == "2":
            name = input("name : ")
            for i in dict:
                if name in i:
                    print(dict[name])

        # In this section, we get the user's name and delete its number from the dictionary by searching the dictionary
        elif select == "3":
            name = input("name : ")
            for i in dict:
                if name in i:
                    del dict[name]
                    print(dict)
                    break

        # To exit the user from the program

        elif select == "4":
            print("Good :)")
            break


phonebook()


