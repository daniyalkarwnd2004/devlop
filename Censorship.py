text = input("Please enter the desired text: ").lower()
list_filter = ["donkey", "animal", "fool"]


def sensor(text, list_filter):
    text_new = text.split()
    names = []
    for word in text_new:
        if word in list_filter:
            names.append("*" * len(word))
        else:
            names.append(word)
    return " ".join(names)


print(sensor(text, list_filter))
