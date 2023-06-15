num= int(input(" Enter Numbers:   "))
sum=0

if num > 0:
    for n in range(0, num) :
        average= float(input("Enter Numer :  "))
        sum += average
    avg = sum/num
    print("sum of the numbers:", sum, "Average is equal to:", avg)

else:
  print("Enter a Valid Number")

