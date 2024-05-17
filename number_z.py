
def number(n):
    p = 1
    for i in range(n, 0, -1):
        print(i, end='\t')
        p = p * i
    print("\nMultiply is ", p)


n = int(input("number : "))
number(n)
