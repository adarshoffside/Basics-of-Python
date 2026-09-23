n = int(input("n: "))   # number of terms

a1 = 0
a2 = 1

print(a1)
print(a2)

term = 3

while term <= n:
    a3 = a1 + a2
    print(a3)

    a1 = a2
    a2 = a3

    term = term + 1