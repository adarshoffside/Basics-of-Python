#sum of first and last digit of a number

n=int(input("n: "))
L=n%10
while n>=10:
    r=n//10
L=L+r
print("Sum of first and last digit:", L)