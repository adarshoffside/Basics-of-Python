n = int(input("n:"))
count = 0
for a in range ( 1,n+1):
    if n%a==0:
        count=count+1
if count==2:
    print("prime")
else:
    print("not prime")