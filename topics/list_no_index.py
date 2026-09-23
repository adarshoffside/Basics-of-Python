L=[12,5,485,8,55,4,66,88,749,97,54,648,48,10,0,3,15]
print(len(L))
print(max(L))
print(min(L))
print(sum(L))

#list slicing
L=[12,5,485,8,55,4,66,88,749,97,54,648,48,10,0,3,15]
#list[startindex:endindex:step]
L1=L[4:11]
print(L1)
#alternative element
L2=L[0:17:2]
print(L2)
#reverse list
L3=L[-1:-18:-1]
print(L3)
#by default


#whole list
print(L[::])
#index 5 to end
print(L[5:])
#satrt to index 9
print(L[:10:])
#step of 2
print(L[::2])
#indx 1 till last
print(L[1:3])


L=[12,5,485,8,55,4,66,88,749,97,54,648,48,10,0,3,15]
print(L[-1])
print(L[-5])
print(L[:-5])
print(L[-1::-1])
print(L[::-1])
print(L[-1:-1:-1])    #empty list
