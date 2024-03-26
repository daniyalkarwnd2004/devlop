
def number_text():
    dict = {}
    text = input("Enter Text : ").split(" ")
    for i in text:
        c = text.count(i)
        dict.update({i: c})
    print(dict)


number_text()