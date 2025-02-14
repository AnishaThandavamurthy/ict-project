#union of sets

old_price = {25 , 85 , 75 , 61 }
new_price = {45, 87, 96, 23}

a=old_price.union(new_price)
print(a)

#intersection


old_price = {25 , 85 , 75 , 61 }
new_price = {45, 87, 96, 23 , 25}

b=old_price.intersection(new_price)
print(b)

#difference


old_price = {25 , 85 , 75 , 61 }
new_price = {45, 87, 96, 23}

c=old_price.difference(new_price)
print(c)