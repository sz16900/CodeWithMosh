# bad example of multiple inheritance


class Employee:
    def greet(self):
        print("Employee greet")


class Person:
    def greet(self):
        print("Person greet")


class Manager(Employee, Person):
    pass


manager = Manager()
manager.greet()


# good example of multiple inheritance

class Flyer:
    pass


class Swimmer:
    pass


class FlyingFish(Flyer, Swimmer):
    pass
