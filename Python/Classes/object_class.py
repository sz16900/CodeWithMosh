class Animal:

    def __init__(self):
        self.age = 1

    def eat(self):
        print("nom nom nom")


class Mammal(Animal):
    def walk(self):
        print("walk")


class Fish(Animal):
    def swim(self):
        print("swim")


m = Mammal()
m.eat()
print(isinstance(m, Animal))
print(isinstance(m, object))
o = object()  # the object class
print(isinstance(Animal, object))
