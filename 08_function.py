def new_function(para, para_one):
    result = para + para_one
    return result


# Adding defaults to your function see below, after one default added, all para right of default
# must also default

def next_function(no, first_name="bob", last_name="jones"):
    return "{0}, {1}, {2}".format(no, first_name, last_name)


print(next_function(1))
# You can pass by name too, see below, additionally, you can't use a pos arg after a key word arg
print(next_function(1, first_name="Ed"))


# Passing pos arguments will fail
def force_function(*, no=0, first_name="bob", last_name="jones"):
    return "{0}, {1}, {2}".format(no, first_name, last_name)


# Unpacking with functions
# You might recall our unpacking tuple example, below is a folow-on
def unpack_function(a, b, c):
    return a, b, c


new_tup = "One", "Two", "Three"
unpack_function(*new_tup)


# Variadic functions have a variable input, like rest in js and ... in Java
def variadic_function(a, b, *z):
    return a, b, z


# Variables in functions are local by default, so using the global keyword we can change their accessibility
var = 1
result = 3


# kwargs

def print_vat(**kwargs):
    print(kwargs)


print_vat(vatpc=15, gross=9.55, message='Summary')
argsdict = dict(vatpc=15, gross=9.55, message='Summary')
print_vat(**argsdict)


def scope_test2():
    global result


scope_test2()
print(result)


# Nested functions
def outer_func():
    print("Outer function!")

    def inner_func():
        print("inner function!")

    inner_func()


outer_func()


# Usecase
def str_out_function(val):
    def inner():
        print(f"{val}")

    inner()


str_out_function("Str")


# lamda
def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(4)

print(mydoubler(12))

# Simple lamda
# Values on the right hand side are the functionality of the object, values on the left hand side are the parameters.
addition = lambda a, b: a + b
print(addition(1, 2))

# Intermed Example
# Here we'll start to use inbuilt functionality:
my_list = [1, 2, 3, 4, 5, 6]
# A new list using the filter function to return a list with a lambda expression
filter_list = list(filter(lambda i: (i % 2 == 0), my_list))
for i in filter_list:
    print(i)
print()
# reduction, essentially addition to a single int value
import functools as ft

# This will take value from the right, and add it to the left, e.g.
i = ft.reduce((lambda x, y: x + y), my_list)
print(i)
# map, applies the right hand arg to the iterated parameter input
# n = 1 * 1, 2 * 2, etc, list out put is n**2
map_list = list(map(lambda n: 2 ** n, my_list))
for i in map_list:
    print(i)

# If we look at this for strings, we can use a string method the iterable, see below:
str_list = ["value", "value", "value", "value", "value", "value"]
map_str = list(map(lambda s: s.capitalize(), str_list))
print(map_str)


# function annotations

def print_vat(**kwargs: 'VAT, gross and message'):
    print(kwargs)


print(print_vat.__annotations__)


def slice(string: str, start: int, end: int) -> str:
    return start


# nonlocal variables

def myfunc1():
    x = "John"

    def myfunc2():
        nonlocal x

    myfunc2()
    return x


print(myfunc1())


def simple_args(*args):
    print(args)

