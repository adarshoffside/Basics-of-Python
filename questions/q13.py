#count all the factors of input n excluding n
#print all the factors of input n excluding n
#print the sum of all the factors of n excluding n

n = int(input("n:"))

count = 0
total = 0
print("All factors of " , n , "including n are")
for a in range (1,n):
    if n%a==0:
        count = count+1
        total=total+a
print("total factors of ",n,"is=",count)
print("total sum of all factors including n are ",total)