# This is a simple Python program
# This program is not connected to the database
# The values ​​you enter will be deleted from the database due to non-use

import datetime


def todo():
    print("1 :the show \n2 :add work \n3 :delete work\n4 :edit work \n5 :Exit the program")
    my_todo = []
    while True:
        work = input("Do you want to add a program ? ")
        if work == "1":
            print(my_todo)
        elif work == "2":
            try:
                date_input = input("date : ")
                day, month, year = map(int, date_input.split("/"))
                date = datetime.date(year, month, day)
                daily_tasks = input("daily tasks : ")
                my_todo.append([date, daily_tasks])
            except ValueError as value:
                print("please enter date :)"), value
        elif work == "3":
            work_delete = input("work : ")
            for i in my_todo:
                if work_delete in i:
                    index_work = my_todo.index(i)
                    del my_todo[index_work]
                    print("delete :)")
                    break
                else:
                    print("not found")
                    break
        elif work == "4":
            work = input("work : ")
            for i in my_todo:
                if work in i:
                    try:
                        edit_work = input("edit work : ")

                        date_input = input("date : ")
                        day, month, year = map(int, date_input.split("/"))
                        date = datetime.date(year, month, day)
                        index_work = my_todo.index(i)
                        my_todo[index_work] = [edit_work, date]
                    except ValueError as value:
                        print("please enter date :)"), value
                else:
                    print("not found")
                    break
        elif work == "5":
            print("good bey")
            break
        else:
            print("please enter correctly :)")


todo()
