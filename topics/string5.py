S=input().split()
L=list(map(int,S))
print(L)
i = int(input())
if i>= len(L) or i<-(len(L)):
    print("Invalid Index")
else:
    element = str(L[i])
    print(len(element))