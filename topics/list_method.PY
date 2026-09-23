L=[12,5,485,8,55,4,66,88,749,97,54,648,48,10,0,3,15,97]
#APPEND (- add new element at the end of the list)
L.append(1000)
print(L)
#insert()
L.insert(0,0) #add new element at given index loc
print(L)
#extend()
L1=[-1,-56,12,-45]
L.extend(L1)
print(L)
#remove
L.remove(88)
print(L)

#pop
#L.pop()
print(L)

#clear
#L.clear()
print(L)

#count
x=L.count(97)
print(x)

#index( )-return the first index occurance  of elemnt
#copy()- creates shallow copy

M=L.copy()
print(M)



#reverse()
L.reverse()
print(L)

#sort()-in ascending order
L.sort()
print(L)

L.sort(reverse=True)
print(L)