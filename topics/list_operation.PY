L1=[1,2,3]
L2=[4,5,6]
L=L1+L2
print(L)

L3=L1*3

print(L3)

#ITERATE FOR LOOP OVER THE LIST
M=[1,2,1,2,5,65,46,64,7,64,75,12,15,26,15,45,100]

for a in M:          #direct fetch method
    print(a)

for a in range (len(M)):          #index conversion method
    print(M[a])



#list comprehension- NL=[exp for loop if cond]

L=[12,5,485,8,55,4,66,88,749,97,54,648,48,10,0,3,15]
NL1=[a for a in L if a%2==0]
NL2=[b for b in L if b%2==1]

print(NL1)
print(NL2)