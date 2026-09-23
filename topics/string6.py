S1= input().split(',')
L= list(map(int(S1)))
S2=input().split(',')
M=list(map(int(S2)))
R=[]
for x in L:
    if x not in M:
        R.append(x)
print(R)