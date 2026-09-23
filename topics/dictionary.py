student = {'NAME': 'Adarsh Yadav'  ,
           'REGISTRATION NO.': 12345678,
           'ROLL NO.': 49,
           'SECTION': 'K3P26BT',
           'BRANCH': 'CSE'
           }

print(student)

#length

print(len(student))

#DICTIONARY IS MUTABLE

#ACCESS VALUE FROM SPECIFIED KEY. HOW?
#HERE IT IS ->

print(student['NAME'])
print(student['REGISTRATION NO.'])
print(student['SECTION'])
print(student['ROLL NO.'])
print(student['BRANCH'])



#ADD NEW KEY VALUE PAIR.?

student['CGPA'] = 9.3


#FOR VERIFYING IT IS ADDED OR NOT WE WILL PRINT IT AGAIN TO SEE THAT.


#UPDATE VALUE FOR ANY SPECIFIED KEY

student['BRANCH'] = 'CSE AI& ML'
print(student)

#KEYS()

print(student.keys())

#VALUES()
print(student.values())

#ITEMS
print(student.items())

#Update()
student.update({'CGPA': 9.5})
print(student)

#Get()
print(student.get('NAME'))