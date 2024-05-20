def family_costs():
    month_list = []
    year_list = []
    while True:
        id_family = int(input("id family : "))
        if id_family == -1:
            break
        family = int(input("costs : "))
        month = family * 31
        year = month * 12
        month_list.append([month, id_family])
        year_list.append([year, id_family])
    print("max month : ", max(month_list))
    print("max year : ", max(year_list))
    print("min month : ", min(month_list))
    print("min year : ", min(year_list))


family_costs()
