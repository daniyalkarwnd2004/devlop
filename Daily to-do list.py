# This program takes the list of daily tasks from the user
def work():
    list_work = []
    while True:
        # In this program, the user can enter, delete and edit their work
        print("select :\n1:Daily Tasks\n2:Eliminate Daily Tasks\n3:Edit\n4:exit")
        select = input("select : ")
        if select == "1":
            text = input("text : ")
            list_work.append(text)
            print(list_work)
        elif select == "2":
            text = input("text : ")
            for i in list_work:
                if text == i:
                    list_work.remove(text)
                else:
                    print("please your text :)")
            print(list_work)
        elif select == "3":
            text = input("text : ")
            for i in list_work:
                if i == text:
                    t = input("text edit:")
                    a = list_work.index(i)
                    list_work[a] = t
                else:
                    print("please your text :)")
            print(list_work)
        elif select == "4":
            print("Good :)")
            break


work()