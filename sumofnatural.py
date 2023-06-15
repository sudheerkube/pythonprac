def natnum(num1):
    sum = 0 
    while (num1 > 0): 
        sum = sum+num1
        num1 = num1-1
    return(sum)


num1  = int(input("Enter the nos: "))
nump = natnum(num1)
print(nump)

