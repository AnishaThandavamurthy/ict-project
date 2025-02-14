#class and object
class MyClass:
    variable="some texxt"

    def myFunction(self):
        print("This is message inside class")

myObjects=MyClass() #creating an instance of the object
myObjects.myFunction()

#using different methods in same class
class myClass():
    def method1(self):
        print("vvit")

    def method2(self,someString):
        print("Project training:"+ someString)

c = myClass()
c.method1()
c.method2("Training is fun")

#ex1
#simple class for a movie

class Movie():
    def func(self,name):

        print("The hero name is"+name)

    def method(self,heroine,language,):
        print("Heroine is",heroine,"released in"+language)

a=Movie()
a.func("Vijay")
a.method("Trisha","tamil")

#ex2
class Movie1():
    lang="English"
    type="action"

    def rating(self):
        print("It has 4 rwating")

    def duration(self,someString):
        print("It is of 3 hours"+someString)

b=Movie1()
b.rating()
a.duration("Marvelous")