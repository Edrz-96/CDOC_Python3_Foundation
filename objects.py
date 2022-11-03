class Person:

    def __init__(self, first_name, last_name, age):  # Constructor
        self.first_name = first_name  # self = this, refers to the instance
        self.last_name = last_name
        self.age = age


# Overloading
def full_name(self):
    return f'{self.first_name} {self.last_name}'


def full_name(self, middle_name):
    return f'{self.first_name} {self.last_name}, {middle_name}'


# Overriding
def age_func(self):
    print("You're old!")


def age_func(self):
    print(self.age)
