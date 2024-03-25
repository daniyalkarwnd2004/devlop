# This program checks whether your email is correct or not. If it says "error" or "no", it means that your email is wrong

def func_email(email):

    symbol = "~!#$%^&*()}{:?><,+*-[]';/"
    gmail = ".@gmail.com"
    yahoo = ".@yahoo.com"
    for i in symbol:
        if i in email:
            print("Error")
            break
    if email.endswith(gmail):
        print("True")
    elif email.endswith(yahoo):
        print("True")
    else:
        print("False")


email = input("Please Your Enter Email :")
func_email(email)
