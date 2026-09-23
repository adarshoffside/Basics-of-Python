#print all the values from range(a,b) that are divisible by
#3 and 5 both


a = int(input("a:"))
b = int(input("b:"))
for x in range (a,b+1):
    if x%3==0 and x%5 ==0:
        print(x,end= " ")