#print all the pri me no between 1 to 1000


print("All prime no between 2 to 1000 are")
pc=0
for n in range (2,1001):
    count = 0
    for a in range (1,n+1):
        if n%a==0:
            count = count+1
    if count==2:
        pc = pc+1
        print(n)
print("total prime nos :",pc)