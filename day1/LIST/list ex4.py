#list operations
#concatenation of two lists
list_yesterday = [17 , 16 , 15]
list_today = [9 , 8 , 6]

list_combined = list_yesterday + list_today
print(list_combined)

#nested list 
customer_1 =["Ananya" , 20]
customer_2 =["Kavya" , 25]
customer_3 =["Harshini" , 30]
customer_4 =["Nisarga", 35]

customers = customer_1 + customer_2 + customer_3 + customer_4

print(customers)


#list of tuples

#iterating through list 
customer_1 =["Ananya" , 20]
customer_2 =["Kavya" , 25]
customer_3 =["Harshini" , 30]
customer_4 =["Nisarga", 35]

customers = customer_1 , customer_2 , customer_3 , customer_4
print(customers)


for i in customers:
    print(i)

#len function
print(len(customers))