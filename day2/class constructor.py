#constructor calling ex1
class Person:
    def __init__(self,name):
        self.name=name

p=Person('sharanya')
print(p.name)
print(p)

#ex2
class person:
    def __init__(self,firstname,lastname,age,country,city):
        self.firstname = firstname
        self.lastname = lastname 
        self.age = age
        self.country=country
        self.city=city

a=person('Ananya','Nagaraj',25,'Karnataka','Mandya')
print(a.firstname)
print(a.lastname)
print(a.age)
print(a.country)
print(a.city)


#ex3
class Person1:
    def __init__(self,firstname='kavya',lastname='jayram',age=21,country='karnataka',city='mysore'):
        self.firstname = firstname
        self.lastname = lastname 
        self.age = age
        self.country=country
        self.city=city

    def person_info(self):
        return f'{self.firstname} {self.lastname} {self.age} {self.country} {self.city}'
s=Person1()
print(s.person_info()) 
s=Person1('anusha','sujay',25,'india','mysuru')
print(s.person_info)