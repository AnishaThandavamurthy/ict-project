#{} for crested 
#[] for 
#mutable and unoredred

students={'Name':'Ananya','Age':21,'Branch':'ISE'}

print(students)
print(type(students))

#operations
#add
students['college'] = 'VVIT'
print(students)

#access value
students['marks']=[40,45,48,50,49]
print(students)

print(students['Name'])

print(students.get('Age'))

#update an existing value
print("before update")
print("students")
print("\n")

students['Age']=30

print("After update")
print(students)

#remove an element from dict
del students['Age']
print(students)

#checking type
#len()
#print()
#get values
print(students.items())

#get all the values
print(students.values())

#get all the key
print(students.keys())