class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def introduceyourself(self):
        print("My name is" +self.name)
        print("My age is" +str(self.age))

class Teacher(Person):
    def stateprofession(self):
        print("I am not a teacher")

author=Teacher("Rakesh",30)
author.introduceyourself()
author.stateprofession()

