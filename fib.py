# index = int(input("Enter recurisve: "))
# firstnum = 0
# secondnum = 1
# temp = 0

# #print(firstnum)
# #print(secondnum)
# for i in range(0,index):
#     temp = firstnum + secondnum
#     firstnum = secondnum
#     secondnum = temp
#     print(temp)

# series 0, 1, 1, 2, 3, 5, 8, 13, 21, 34

# def fibonacci(i):
#         if i==0:
#             return 0
#         elif i==1:
#             return 1
#         else:
#             return fibonacci(i-2) + fibonacci(i-1)

# index=int(input("Enter the index till you want the series : "))
# if index <= 0:
#     print("Please add a positive number!")
# else:
#     for i in range(0, index):
#         print(fibonacci(i))

# series 0, 1, 1, 2, 3, 5, 8, 13, 21, 34

index=int(input("Enter the index till you want the series : "))

firstNumber=0
secondNumber=1
temp=0

print(firstNumber)
print(secondNumber)
for i in range(0, index):
    temp = firstNumber + secondNumber
    firstNumber = secondNumber
    secondNumber = temp
    print(temp)