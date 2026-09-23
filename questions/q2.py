#check the given alphabet is upper , lower , digit or special

ch = str(input("character:"))
if ord(ch) >= 65 and ord(ch)<=90:
    print(ch , "is upper case alphabet") 

elif ord(ch) >= 97 and ord(ch) <= 122:
    print(ch , " is lower case alphabet")

elif ord(ch) >= 48 and ord(ch) <= 57:
    print(ch,"is digt")
else:
    print(ch,"special character")