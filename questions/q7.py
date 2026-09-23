# odd even

n = int(input("n: "))

ev = 0
od = 0

while n != 0:
    r = n % 10

    if r % 2 == 0:
        ev = ev + 1
    else:
        od = od + 1

    n = n // 10

print("Even", ev)
print("Odd", od)