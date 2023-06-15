var1 = int(input("Any number between 1-100: "))
result = ''
if (var1 > 0 and var1 < 100):
  for i in range(0, var1+1):
    result = result + str(i)
  print(result)

elif (var1 == 0):
  print("Enter nothing")

else:
  print("Out of range index number")

