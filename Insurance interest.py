def calculate_insurance_profit(capital, interest_rate, years):
    total_profit = capital * (interest_rate / 100) * years
    return total_profit


capital = float(input("Please enter the investment amount:"))
interest_rate = float(input("Please enter interest percentage:"))
years = int(input("Please enter the number of years:"))

profit = calculate_insurance_profit(capital, interest_rate, years)
print("Insurance benefit for", years, "Year with investment", capital, "as a percentage of profit", interest_rate,"Equal to", profit, "Is.")