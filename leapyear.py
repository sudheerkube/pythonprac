def is_leap(year):
    if (( year % 400 ==0 ) | (year % 100 !=0 ) & (year %4 == 0)):
        return True
    else:
        return False

year = int(input("Enter the leap year:  "))
print(is_leap(year))

    