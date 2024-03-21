def shop():
    dict = {}
    while True:
        print("1: Add product\n2: search\n3: delete\n4: the show\n5: Show price\n6: exit\n")
        select = input("select : ")
        # We will add this part of the products to the dictionary

        if select == "1":
                name = input("name : ")
                Price = int(input("Price : "))
                dict.update({name: Price})
                if name == " ":
                    print("Exit:)")
                    break
        # In this section, we search for the product we want

        elif select == "2":
            name = input("name : ")
            for i in dict:
                if name in i:
                    print(dict[name])

        # In this section, we remove the product we want from the list of products
        elif select == "3":
            name = input("name : ")
            for i in dict:
                if name in i:
                    del dict[name]
                    print(dict)
                    break

        # In this section, we display our products
        elif select == "4":
            print(dict.keys())

        # In this section, we enter the name of the product and see its price
        elif select == "5":
            name = input("name : ")
            for i in dict:
                if name in i:
                    print(dict[name])

        # In this part, we leave the program
        elif select == "6":
            print("Good :)")
            break


shop()


