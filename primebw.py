# num1 = int(input("First number: "))
# num2 = int(input("Second number: "))

# for pri in range(num1,num2+1):
#     for j in range(2, pri):
#         if((pri%j)==0):
#             print(pri,"is not prime")
#             break
#     else:
#         print(pri,"is prime number")
#############################################################################################

def primeOrNot(First, Second):
    for i in range (First, Second+1):
        for j in range(2, i):
            if((i%j)==0):
                print (i, "is not a prime number")
                break
        else:
            print(i, "is a prime number")

FirstInterval=int(input("Please enter the First interval : "))
SecondInterval=int(input("Please enter the Second interval : "))

if ((FirstInterval > 1 and SecondInterval > 2) and FirstInterval < SecondInterval):
    primeOrNot(FirstInterval, SecondInterval)
else:
    print("Enter a valid range!")