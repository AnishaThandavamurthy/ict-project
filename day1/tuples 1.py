numbers = (21 , 43 , 544 , 76 , 87 , 977 , 21 , 5 , 255)
print(numbers)
fruits = ('banana' , ' apples' , 'grapes')
print(fruits)

print(numbers[4])

#multiple datatypes can be listed togrther

print(type(numbers))

#[] = list
#() = tuple

#tuple indexing is similar to list indexing
#slicing a tuple

a=numbers[4:]
print(a)

b=numbers[0:4]
print(b)

#repeat tuples
#check 'in' or 'not in'
#iterating through tuples

for i in fruits:
    print(i)
#len()
print(len(fruits))

#max(),min() 
#sorted()
#del()

del (numbers[5])
print(numbers)

#tuple doesnt support deleting an item
#complete tuple will be deleted
#parenthesis is not compulsory in tuples

