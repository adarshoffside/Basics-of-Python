#range()   ->  range(start,stop,step)
#range(11,21) -> range(11,21,1) -> 11  12  13 .....20
#range(1,21,2)  -> 1 3 4 5 6....21
#range(10) -> range(0,10)


for a in range(10,20,1):
    print(a)

d=17

print(d in range (17))

print(d not in range(17))

print(d-1 in range(16))

#range(start,stop,step)

for q in range(10, 0, -1):
    print(q)


print(17 in range (18,0,-2))