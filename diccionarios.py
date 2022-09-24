student = {'name': 'john', 'age': 25, 'courses': ['Math', 'CompSci']}

print(student.get('phone', 'Not found'))

student['phone'] = '091247770'
print(student.get('phone', 'Not found'))

student.update({'name': 'Jane', 'age': 26})
print(student)

del student['age']
print(student)

phone = student.pop('phone')
print(phone)
print(student)

print(student.keys())
print(student.values())
print(student.items())

for key, value in student.items():
    print(key, value)