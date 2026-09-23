n = int(input("n: "))
count = 0
for i in range(1, n + 1):
    if n % i == 0:
        count += 1

if count == 2 or count ==1:
    print("prime number")
else:
    print("not a prime number")