man = 0
female = 0
rights_man = 0
rights_female = 0
while True:
    id_persons = int(input("id persons : "))
    if id_persons == -1:
        break
    year_of_employment = int(input("year of employment : "))
    if 2000 > year_of_employment > 2025:
        print("Error")
    gender_code = int(input("gender code  [1 = man] [2 = female] : "))
    if gender_code == 1 or gender_code == 2:
        if gender_code == 1:
            man += 1
            rights = int(input("rights : "))
            rights_man += rights
        elif gender_code == 2:
            female += 1
            rights = int(input("rights : "))
            rights_female += rights
    else:
        print("Error")
        break
try:
    average_salary_of_men = rights_man / man
    print("number of male employees : ", man)
    print("average salary of men : ", average_salary_of_men)
except ZeroDivisionError as zero:
    print("on person", zero)
try:
    average_salary_of_women = rights_female / female
    print("number of female employees : ", female)
    print("average salary of women : ", average_salary_of_women)
except ZeroDivisionError as zero:
    print("on person", zero)
