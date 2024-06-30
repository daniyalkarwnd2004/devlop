def year(year1: int, year2: int):
    nt = (year2 - year1) / year1
    year3 = year1 + year2 * nt
    print("%", nt, "\t", year3)


y = int(input("number : "))
y1 = int(input("number : "))
year(y, y1)
