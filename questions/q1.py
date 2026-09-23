#that accepts 4 separate inputs  integrs and print the larger among them.

num1 = int(input("num1:"))
num2 = int(input("num2:"))
num3 = int(input("num3:"))
num4 = int(input("num4:"))


if num1>= num2 and num1>= num3 and num1 >=num4:
    print("Largest Number :" ,num1)

elif num2>= num3 and num2>= num4 and num3 >=num1:
    print("Largest Number :" ,num2)

elif num3>= num2 and num3>= num4 and num3 >=num1:
    print("Largest Number :" ,num3)

else:
    print("Largest Number is:" , num4)