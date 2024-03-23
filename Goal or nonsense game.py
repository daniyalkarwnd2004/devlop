from random import choice


def game():
    u = 0
    c = 0
    while True:
        computer = choice(["r", "l"])
        user = input("Enter User [R/L] :").lower()
        if user == "l" and computer == "r":
            print("user win")
            u += 1
            print(f"user {u}")
            c -= 1
            print(f"- computer {c}")
        elif user == "r" and computer == "l":
            print("user win")
            u += 1
            print(f"user {u}")
            c -= 1
            print(f"- computer {c}")
        elif user == "l" and computer == "l":
            computer = "win"
            print("computer", computer)
            c += 1
            print(f"computer {c}")
            u -= 1
            print(f"- user {u}")
        elif user == "r" and computer == "r":
            computer = "win"
            print("computer", computer)
            c += 1
            print(f"computer {c}")
            u -= 1
            print(f"- user {u}")
        elif user == "exit":
            break
        else:
            print("error")
    if u > c:
        print("User Win !!!!")
    elif c > u:
        print("Computer Win !!!!")
    print("pon user", u)
    print("pon computer", c)


game()
