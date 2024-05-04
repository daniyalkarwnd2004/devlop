# This is a simple library management application
# Due to the lack of use of classes, program code inheritance is high and repetitive
# Due to the lack of connection to the database, this program automatically deletes
# the values, and we have to enter values for each series
# Due to the lack of connection to the database, this application does not work properly,
# that is, it does not work like a real application
# Due to the use of repetitive codes in this program,
# the speed of the program is low and the number of lines of code in this program is high
# Attention !!!!
# This is a simple program just for learning, not a project, that's why this program is full of programming bugs


def libre():
    global name_book1, the_writer1, year1, location1, genre1, name_book2, the_writer2, year2,\
        location2, genre2, name_book3, the_writer3, year3, location3, genre3, name_book4, the_writer4,\
        year4, location4, genre4, name_books1, name_books2
    name_user = {}
    name_books1 = {}
    while True:
        print("select :\n1-show books\n2- register \n3-add book\n4-login user\n5- show contacts\n6-popular books")
        select = input("select : ")
        if select == "2":
            name = input("name : ")
            family = input("family : ")
            national_code = int(input("national_code : "))
            if national_code > 10 > national_code:
                national_code = int(input("national_code : "))
            phone_number = int(input("phone_number : "))
            if phone_number > 11 > phone_number:
                phone_number = int(input("phone_number : "))
            name_user.update({national_code: [name, family, phone_number]})
        elif select == "5":
            username = input("username : ")
            password = input("password : ")
            if password == "Aa123456" and username == "admin":
                print(name_user)
            elif password != "Aa123456":
                print("password Error")
            elif username != "admin":
                print("username Error")
            else:
                print("Error")
        elif select == "1":
            print("1: criminal\n2:an adventure\n3:romantic\n4:action")
            type_books = input("type of book :")
            if type_books == "1":
                name_books1 = {
                    "the murderer": ["jim", "2019", "chicago", "criminal"],
                    "accident": ["lucas", "2016", "cork", "criminal"],

                }
                try:
                    for i in name_books1:
                        print(i, name_books1[i])
                    name_books1.update({name_book1: [the_writer1, year1, location1, genre1]})
                    print("update book : ", name_books1)

                except NameError:
                    pass
            elif type_books == "2":
                name_books2 = {
                    "road": ["linda", "2020", "munich", "an adventure"],
                    "beautiful": ["yin", "2014", "venice", "an adventure"],
                    "city": ["primal", "2017", "london", "an adventure"]
                }
                try:
                    for i in name_books2:
                        print(i, name_books2[i])
                    name_books2.update({name_book2: [the_writer2, year2, location2, genre2]})
                    print("update book : ", name_books2)

                except NameError:
                    pass
            elif type_books == "3":
                name_books3 = {
                    "love": ["nazi", "2015", "los angles", "romantic"],
                    "hope": ["sethi", "2020", "paris", "romantic"],
                    "the night": ["anna", "2024", "lstanbul", "romantic"]
                }
                try:
                    for i in name_books3:
                        print(i, name_books3[i])
                    name_books3.update({name_book3: [the_writer3, year3, location3, genre3]})
                    print("update book : ", name_books3)
                except NameError:
                    pass
            elif type_books == "4":
                name_books4 = {
                    "sofi": ["rayon", 2007, "needlework", "action"],
                    "1989": ["mega", 2000, "berlin", "action"]
                }
                try:
                    for i in name_books4:
                        print(i, name_books4[i])
                    name_books4.update({name_book4: [the_writer4, year4, location4, genre4]})
                    print("update book : ", name_books4)
                except NameError:
                    pass
            else:
                print("Error :) \n please enter your select")
        elif select == "3":
            username = input("username : ")
            password = input("password : ")
            if password == "Aa123456" and username == "admin":
                print("1: criminal\n2:an adventure\n3:romantic\n4:action")
                type_books = input("type book :")
                if type_books == "1":
                    name_book1 = input("name : ")
                    the_writer1 = input("the_writer : ")
                    year1 = input("year : ")
                    location1 = input("location : ")
                    genre1 = input("genre : ")

                elif type_books == "2":
                    name_book2 = input("name : ")
                    the_writer2 = input("the_writer : ")
                    year2 = input("year : ")
                    location2 = input("location : ")
                    genre2 = input("genre : ")
                elif type_books == "3":
                    name_book3 = input("name : ")
                    the_writer3 = input("the_writer : ")
                    year3 = input("year : ")
                    location3 = input("location : ")
                    genre3 = input("genre : ")
                elif type_books == "4":
                    name_book4 = input("name : ")
                    the_writer4 = input("the_writer : ")
                    year4 = input("year : ")
                    location4 = input("location : ")
                    genre4 = input("genre : ")
            elif password != "Aa123456":
                print("password Error")
            elif username != "admin":
                print("username Error")
            else:
                print("Error")
        elif select == "4":
            list_book = []
            national_code1 = int(input("national code : "))
            for i in name_user:
                if national_code1 == i:
                    print(f"welcome user {national_code1}")
                    print("1: criminal\n2:an adventure\n3:romantic\n4:action")
                    select_book = input("book :")
                    if select_book == "1":
                        book_select = {
                            "1 : the murderer": ["jim", "2019", "chicago", "criminal"],
                            "2 : accident": ["lucas", "2016", "cork", "criminal"],
                        }
                        for j in book_select:
                            print(j, book_select[j])
                        while True:
                            name_book = input("id book : ")
                            if name_book == "0":
                                break
                            if name_book == "1":
                                list_book.append(book_select["1 : the murderer"])
                            elif name_book == "2":
                                list_book.append(book_select["2 : accident"])
                            else:
                                print("Error")
                    if select_book == "2":
                        book_select = {
                            "1 : road": ["linda", "2020", "munich", "an adventure"],
                            "2 : beautiful": ["yin", "2014", "venice", "an adventure"],
                            "3 : city": ["primal", "2017", "london", "an adventure"]
                        }
                        for j in book_select:
                            print(j, book_select[j])
                        while True:
                            name_book = input("id book : ")
                            if name_book == "0":
                                break
                            if name_book == "1":
                                list_book.append(book_select["1 : road"])
                            elif name_book == "2":
                                list_book.append(book_select["2 : beautiful"])
                            elif name_book == "3":
                                list_book.append(book_select["3 : city"])
                            else:
                                print("Error")
                    if select_book == "3":
                        book_select = {
                            "1 : love": ["nazi", "2015", "los angles", "romantic"],
                            "2 : hope": ["set-hi", "2020", "paris", "romantic"],
                            "3 : the night": ["anna", "2024", "Istanbul", "romantic"]
                        }
                        for j in book_select:
                            print(j, book_select[j])
                        while True:
                            name_book = input("id book : ")
                            if name_book == "0":
                                break
                            if name_book == "1":
                                list_book.append(book_select["1 : love"])
                            elif name_book == "2":
                                list_book.append(book_select["2 : hope"])
                            elif name_book == "3":
                                list_book.append(book_select["3 : the night"])
                            else:
                                print("Error")
                    if select_book == "4":
                        book_select = {
                            "1 : sofi": ["rayon", 2007, "needlework", "action"],
                            "2 : 1989": ["mega", 2000, "berlin", "action"]
                        }
                        for j in book_select:
                            print(j, book_select[j])
                        while True:
                            name_book = input("id book : ")
                            if name_book == "0":
                                break
                            if name_book == "1":
                                list_book.append(book_select["1 : sofi"])
                            elif name_book == "2":
                                list_book.append(book_select["2 : 1989"])
                            else:
                                print("Error")
            print(list_book)
        elif select == "6":
            book = ["1989", "love"]
            print("1: show popular books \t 2: add popular book")
            popular = input("select : ")
            if popular == "1":
                print(book)
            elif popular == "2":
                name_book_popular = input("name book : ")
                book.append(name_book_popular)
            else:
                print("Error")
            print(book)


libre()
