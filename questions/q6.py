n=int(input("n: "))
org = n
rev = 0
while n!=0:
    r=n%10
    rev=rev*10+r
    n=n//10
print(" Rev =",rev)
if org==rev:
    print("Palindrome")

else:
    print("Not palindrome")