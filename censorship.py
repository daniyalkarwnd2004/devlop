def censorship(words):
    print("****-------censorship-------****")
    w = None
    while True:
        word = yield w
        if word not in words:
            w = word
        else:
            w = "*" * len(word)


gn = censorship(["donkey", "cow", "unconscious", "fool"])
next(gn)
print(gn.send("ali"))
print(gn.send("fool"))
