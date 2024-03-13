from functools import wraps


def dec(func):
    @wraps(func)
    def inner(text):
        while True:
            print("Please select  \n1)Encryption\n2)Decoding\n3)Exit")
            select = input("Please enter your selection : ")
            if select == "1":
                def encryption(text1):
                    encryption_text = ""
                    for char in text1:
                        x = ord(char) * 2 + 5
                        encryption_text += chr(x)
                    print("Encrypted text : ", encryption_text)
                encryption(text)
            elif select == "2":
                def decoding(text1):
                    decoding_text = ""
                    for char in text1:
                        x = (ord(char) - 5) // 2
                        decoding_text += chr(x)
                    print("Decoding text : ", decoding_text)
                decoding(text)
            elif select == "3":
                print("Good :)")
                break
    return inner


@dec
def placement(text):
    print(text)


Text = input("Please Text : ")
placement(Text)
