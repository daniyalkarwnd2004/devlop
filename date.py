from persiantools.jdatetime import JalaliDate
from functools import wraps
import datetime


def dec(func):
    @wraps(func)
    def inner(fromdate, todate):
        print("date : solar and ad")
        if fromdate == "solar".lower() and todate == "ad".lower():
            day = int(input("Enter Day : "))
            month = int(input("Enter Month : "))
            year = int(input("Enter Year : "))
            ad = JalaliDate(year, month, day).to_gregorian()
            print(f"Date in AD : {ad}")
        elif fromdate == "ad".lower() and todate == "solar".lower():
            day = int(input("Enter Day : "))
            month = int(input("Enter Month : "))
            year = int(input("Enter Year : "))
            solar = JalaliDate(datetime.date(year, month, day))
            print(f"Date in solar : {solar}")
        else:
            print("Error")
    return inner


@dec
def func_year(solar, ad):
    print(solar)
    print(ad)



solar = input("From_Date : ")
ad = input("To_Date : ")
func_year(solar, ad)


