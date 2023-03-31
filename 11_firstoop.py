class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


class Employee(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.firstname = fname
        self.lastname = lname

bob = Employee("Bob", "Bobson")
bob.printname()


class Animal:
    def __init__(self, _type):
        self.type = _type


class Mammal(Animal):
    def __init__(self, mammal_name):
        print(mammal_name)
        super().__init__(mammal_name)


dog = Mammal("Dog")
print(dog.type)


