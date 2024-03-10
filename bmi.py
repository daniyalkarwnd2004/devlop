
# we take the height and weight to do the calculation
def bmi(height, weight):

    # We receive the height and weight from the user and calculate them with the following formula
    
    bmi_project = (weight / (height ** 2))

   Using the conditions, we calculate the body mass index equation # 
    
    if bmi_project < 18.5:
        print("underweight")
    elif bmi_project >= 18.5 and bmi_project <= 24.9:
        print("healthy weight")
    elif bmi_project  >= 25.0 and bmi_project <= 29.9:
        print("obesity => class one")
    elif bmi_project >= 30.0 and bmi_project <= 34.9:
        print("obesity => class two")
    elif bmi_project >= 35.0 and bmi_project <= 39.9:
        print("obesity => class three")


height1 = float(input("height : "))
weight1 = float(input("weight : "))
bmi(height1, weight1)
