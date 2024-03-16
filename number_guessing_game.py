import random


def play(number, question):

    c = random.randint(1, 20)
    while question != "t":
        if number > 20:
            print("Error")
            break
        if question == "s":
            c += 1
            print(c)
            question = input("question : ")
        if question == "g":
            c -= 1
            print(c)
            question = input("question : ")
    print("computer Win !!!")


digit = int(input("number : "))
ques = input("question : ")
play(digit, ques)