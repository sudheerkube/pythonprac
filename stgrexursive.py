def revstring(string):
    newstring = ""
    for i in string:
        newstring = i + newstring
    return(newstring)

string = input("Ennter the string:   ")
strlen = revstring(string)
print(strlen)
