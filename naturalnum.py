def pnz(vals):
    if vals > 0:
        print("Positive no")
    elif vals == 0:
        print("It's a Zero")
    else:
        print("It's a Negative number")

num= int(input(" Enter Numbers:   "))
pnz(num)