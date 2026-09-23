#slicing in the string 
#read the set of characters
#str[start_index:end_index:step]

STR = "Lovely Proffesional University"
STR1 = STR[0:6]
STR2 = STR[7:19]
STR3 = STR[20:30]

print(STR1)
print(STR2)
print(STR3)


newStr = "Apple Banana Guava"  #nahi samjh aya firse padhleeee
print(newStr[5::])
print(newStr[:10:])
print(newStr[::2])
print(newStr[-1:])
print(newStr[-1:-6])
print(newStr[:-5]) 
print(newStr[:-5:-1])
print(newStr[:-1:-1])
print(newStr[-5::-1])