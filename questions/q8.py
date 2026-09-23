#input no is armstrong or not


import math as m
n = int(input("n:"))
L = int(m.log10(n))+1

org = n
total= 0
while n!=0:
    r=n%10
    total = total +r**L
    n= n//10

if org ==total:
    print("Armstrong")
else:
    print("Not Armstrong")