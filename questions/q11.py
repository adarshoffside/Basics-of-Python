n = int(input("n: "))

mx = n % 10
mn = n % 10

while n != 0:
    r = n % 10

    if r > mx:
        mx = r

    if r < mn:
        mn = r

    n = n // 10

print("max:", mx)
print("min:", mn)