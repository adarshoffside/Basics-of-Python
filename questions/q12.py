#Perfect no or not
n = int(input("n:"))
s=0
for a in range(1,n):
    if n%1==0:
        s=s+a
if s==n:
    print("perfect no")
else:
    print("not a pefect no")