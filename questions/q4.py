age = int(input("age:"))

if age>=18:
    if age>=60:
        print("Allowed for vote in room 21")
    else:
        print("Allowed for vote in room 22")

else:
    print("Not allowed to vote")