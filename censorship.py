def cen_gen(words):
    w = None
    while True:
        word = yield w
        if word not in words:
            w = word
        else:
            w = "*" * len(word)


gen = cen_gen(["caw", "make", "sheep"])
next(gen)
print(gen.send("ali"))
print(gen.send("caw"))