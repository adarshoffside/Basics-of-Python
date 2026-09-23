# Types: if, if-else, if-elif-else, match-case

#print the square of positive values only.

#if condition:
    #body-set of statements

#elif condition:
    #body of elif

#elif condition:
    #body of elif

#else condition:
    #body of else  (else is always in last)


num =int(input("num:"))
if num>0:
    print("square = " , num*num)

elif num<0 :
    print("cube = " , num**3)

if num%2==0:
    print(num, "is even")

if num&1==0:
    print(num,"is even by this method too")

else:
    print(num,"is odd")



