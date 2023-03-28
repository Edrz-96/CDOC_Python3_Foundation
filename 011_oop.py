class Person:
    no_of_people = 0

    def __init__(self, first_name, last_name, age):  # Constructor
        self._first_name = first_name  # self = this, refers to the instance
        self._last_name = last_name
        self._age = age
        Person.no_of_people += 1

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, new_first_name):
        self._first_name = new_first_name @ property

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, new_first_name):
        self._last_name = new_first_name @ property

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new):
        self._age = new

    def __str__(self):
        return f'{self._first_name}, {self._last_name}, {self._age}'


ed = Person("a", "b", 1)
bob = Person("Bob", "Bobson", 2)
assert isinstance(ed, Person) == True
print(Person.no_of_people)
