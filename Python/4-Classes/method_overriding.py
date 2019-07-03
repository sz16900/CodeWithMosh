# replacing or extending a method defined in the base class
# in this implementation we are extending the __init__


class Animal:

    def __init__(self):
        print("Animal Constructor")
        self.age = 1

    def eat(self):
        print("nom nom nom")


class Mammal(Animal):

    def __init__(self):
        print("Mammal Constructor")
        self.weight = 100
        super().__init__()

    def walk(self):
        print("walk")


class Fish(Animal):
    def swim(self):
        print("swim")


m = Mammal()
print(m.age)
print(m.weight)
