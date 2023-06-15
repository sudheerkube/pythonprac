num1 = int(input("enter num1 :" ))
num2 = int(input("Enter num2: " ))

if num1 < num2 :
    print("bwfore swap", num1,num2)
    num2=num2+num1
    num1=num2-num1
    num2=num2-num1
    print("Afer swap",num1,num2)

else:
    print("Nums",num1,num2)
    num1=num2+num1
    num2=num2-num1
    num1=num2-num1
    print("After swap",num1,num2)