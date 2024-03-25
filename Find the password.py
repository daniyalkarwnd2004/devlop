# This program takes a password from you and finds the password you typed

import os
password = input("Password : ")
list_name = ['q', 'w', 'e', 'r', 't', 'y', 'u',
             'i', 'o', 'p', 'a', 's', 'd', 'f', 'g',
             'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v',
             'b', 'n', 'm', 'Q', 'W', 'E', 'R', 'T',
             'Y', 'U','I', 'O', 'P', 'A', 'S', 'D', 'F',
             'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'G',
             'B', 'N', 'M','~', '!', '@', '#', '$',
             '%', '^', '&', '*', '(', ')', '{', '}',
             '[', ']', '+', '-', '?', '>', '<', ':', '=',
             ';', '/', '0', '1', '2', '3', '4', '5', ".",
             '6', '7', '8', '9']
pas = " "
for line in password:
    for line2 in list_name:
        os.system('cls')
        if line == line2:
            print(line)
            pas += line

print("your password : ", pas)

