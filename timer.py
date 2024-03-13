
# We call time
from time import sleep


def time():

    # We create an infinite loop and display the menu to the user

    while True:
        print("please select \n1_start the timer\n2_exit")
        select = input("select : ")
        if select == "1":

            # We receive hours, minutes and seconds from the user

            hour = int(input("enter hour : "))
            minutes = int(input("enter minutes : "))
            seconds = int(input("enter seconds : "))

            # We add hours, minutes and seconds together and delay one second using sleep

            timer = hour * 60 * 60 + minutes * 60 + seconds
            sleep(1)

            # We create a loop until the timer is greater than 0 and its value decreases by 1 every second

            while timer > 0:
                print(timer)
                sleep(1)
                timer -= 1
        elif select == "2":
            print("good :)")
            break
        else:
            print("error :)")


time()