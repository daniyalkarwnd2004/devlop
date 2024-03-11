file = open("text.txt", "w+", encoding="utf-8")
if file.writable():
    print(file.write("dani"))
else:
    print("Error")