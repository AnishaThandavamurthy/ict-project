class Animal:
    def speak(self):
        print('Animal can sleep')

class Mammal(Animal):
    def walk(self):
        print('Mammal can walk')

class Dog(Mammal):
    def bark(self):
        print('Dog can bark')

d=Dog()
d.speak()
d.walk()
d.bark()

  