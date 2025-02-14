#set{}
number = {21 , 45 , 60 , 75 , 80}
print(number)
print(type(number))

#duplicate number

number = {21 , 45 , 60 , 75 , 80 , 45}
print(number)
print(type(number))

#set is unordered
#len()
print(len(number))

#max(),min()
print(max(number))

#both heterogeneous and homogeneous
#add elements to a set -no specific index it randomly chooses the places
number.add(99)
print(number)

#del element from set
number.remove(99)
print(number)

#delete arbitary element pop()
number.pop()
print(number)

#delete set del()

#union of sets

old_price = {25 , 85 , 75 , 61 }
new_price = {45, 87, 96, 23}

old_price.union(new_price)
print(old_price)