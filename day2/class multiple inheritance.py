class flyer:
    def fly(self):
        print('flying')

class swimmer:
    def swim(self):
        print('swimming')

class duck(flyer,swimmer):
    pass

d=duck()
d.fly()
d.swim()