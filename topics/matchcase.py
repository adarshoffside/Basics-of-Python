#match case statement

#match exp: #choice no
    #case no:
    #code:
    #case no :
    #code:

#print the day using match case

day = int(input("day : "))
match day :
    case 1:
        print("Monday")

    case 2:
        print("Tuesday")

    case 3:
        print("Wednesday")

    case 4 : 
        print("Thursday")

    case 5:
        print("Friday")

    case 6:
        print("Saturday")

    case 7:
        print("Sunday")

    case _:
        print("Wrong choice! Run again")


#demonstrate the use of arithmatic operations using match case


op = input ("Enter operator symbol")
a = int(input("a :"))
b = int(input("b :"))

match op:
    case '+':
        print("Addition =", a+b)

    case '-':
        print("Subtraction =", a-b)

    case '/':
        print("Division =", a/b)

    case '**':
        print(" Exponential=", a**b)

    case '//':
        print("Floor Division =", a//b)

    case "%":
        print("Modulus =", a % b)

    case _:
        print("Wrong choice!")