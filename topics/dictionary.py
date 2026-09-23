student = {
    'NAME': 'Adarsh Yadav',
    'REGISTRATION NO.': 12345678,
    'ROLL NO.': 49,
    'SECTION': 'K3P26BT',
    'BRANCH': 'CSE'
}

print(student)

# LENGTH
print(len(student))


# DICTIONARY IS MUTABLE

# ACCESS VALUE FROM SPECIFIED KEY
print(student['NAME'])
print(student['REGISTRATION NO.'])
print(student['SECTION'])
print(student['ROLL NO.'])
print(student['BRANCH'])


# ADD NEW KEY-VALUE PAIR
student['CGPA'] = 9.3

# VERIFY THAT CGPA IS ADDED
print(student)


# UPDATE VALUE FOR A SPECIFIED KEY
student['BRANCH'] = 'CSE AI & ML'
print(student)


# KEYS()
print(student.keys())


# VALUES()
print(student.values())


# ITEMS()
print(student.items())


# UPDATE()
student.update({'CGPA': 9.5})
print(student)


# GET()
print(student.get('NAME'))


# POP()
student.pop('ROLL NO.')
print(student)


# POPITEM()
student.popitem()
print(student)


 #COPY
student1 = student.copy()
print(student1)

#CLEAR
student1.clear()
print(student1)