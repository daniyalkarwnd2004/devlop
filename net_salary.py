def net_salary(_rights, _tax_percentage, _insurance_deficit):
    global insurance
    tax = _rights * _tax_percentage
    print("tax percentage", tax)
    if _insurance_deficit == 1:
        insurance = _rights * 0.07
        print("insurance deficit", insurance)
    elif _insurance_deficit == 2:
        insurance = _rights * 0.08
        print("insurance deficit", insurance)
    elif _insurance_deficit == 3:
        insurance = _rights * 0.10
        print("insurance deficit", insurance)
    else:
        print("Error")
    rights_tax = tax + insurance
    rights_ = rights_tax - _rights
    print(abs(rights_))


rights = int(input("rights : "))
tax_percentage = float(input("tax percentage : "))
insurance_deficit = int(input("insurance deficit : "))
net_salary(rights, tax_percentage, insurance_deficit)
