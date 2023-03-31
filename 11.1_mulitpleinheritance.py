class Animal:
    def __init__(self, _type):
        self.type = _type


class Mammal(Animal):
    def __init__(self, mammal_name):
        print(mammal_name)
        super().__init__(mammal_name)


class Quadruped(Mammal, Animal):
    def __init__(self, mammal_name, has_four_legs=True):
        super().__init__(mammal_name)
        self.has_four_legs = has_four_legs

    def check_quad(self):
        if not self.has_four_legs:
            print("This animal is not a quadruped!!! :(")
        else:
            print("This animal has four legs!!! :)")


zebra = Quadruped("Zebra")
# See default value
zebra.check_quad()
# Check MRO - Method Resolution Order
print(Quadruped.mro())
print(Quadruped.__mro__)
# Look at the order or inheritance, if you changed this would the MRO change?
