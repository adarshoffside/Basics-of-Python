#loops
#for loop
#while loop


#syntax of for loop
#for var in sequance:
    #body of for loop

for a in range(5):
    print("K3P26BT")

#print the table of n using loop

n = int(input("n:"))
for a in range(1,11): #for reverse we will (10,0,-1)
    print(n,"*" ,a, "=",n*a)


#print factorial of given input n

n = int(input("n: "))

f = 1

for a in range(1, n + 1):
    f = f * a

print("Factorial of", n, "is =", f)

i = 1
while i <= 20:
    print(i)
    i += 1



    n=int(input("n: "))
    L=0
    while n!=0:
        r=n%10
        L=L+r
        n=n//10
        print("Sum of digits:", L)