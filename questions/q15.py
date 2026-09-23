#lcm and hcf

a = int(input("a:"))
b = int(input("b"))
m = a*b
while a!=b:
    if a>b:
        a=a-b
    else:
        b=b-a
print('HCF :',a)
print("LCM :",b)