def game_hop(digit):
    while True:
        user = int(input("user : "))
        computer = user + 1

        if user % digit == 0:
            user = input("user :")
            if user != "hop":
                print("user los")
                break
        elif computer % digit == 0:
            computer = "hop"
        print("computer", computer)


number = int(input("number : "))
game_hop(number)
