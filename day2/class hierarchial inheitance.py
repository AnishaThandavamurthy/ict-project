#hierarchial inheitance
class Animal:
    def speak(self):
        print("Animal can speak")

class Dog(Animal):
    def bark(self):
        print("Dog can bark")

class Cat(Animal):
    def meow(self):
        print("Cat can meow")

dog=Dog()
dog.speak()
dog.bark()

cat=Cat()
cat.speak()
cat.meow()