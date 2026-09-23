S=input().split(',')
L=list(map(int,S))
p1=int(input())
p2=int(input())
if p1>=len(S) or p2>=len(S):
    print("Index out of range")
else:
    temp=S[p1]
    S[p1]=S[p2]
    S[p2]=temp
    print(S)