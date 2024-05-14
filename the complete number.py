number_list = []
number = int(input("Enter Number : "))
for i in range(1, number):
    if number % i == 0:
        number_list.append(i)
        print(i)
if sum(number_list) == number:
    print("Yes")
else:
    print("No")
