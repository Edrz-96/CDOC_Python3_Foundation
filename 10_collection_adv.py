# Filter

def check_even(number):
    if number % 2 == 0:
        return True

    return False


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# if an element passed to check_even() returns True, select it
even_numbers_iterator = filter(check_even, numbers)
# converting to list, a filter object is not printable

even_numbers = list(even_numbers_iterator)
print(even_numbers)

letters = ['a', 'b', 'd', 'e', 'i', 'j', 'o']


def filter_vowels(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return True if letter in vowels else False


filtered_vowels = filter(filter_vowels, letters)

# converting to tuple
vowels = tuple(filtered_vowels)
print(vowels)

# List comprehension

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

# Dic comprehension

d = {n: n ** 2 for n in range(5)}
print(d)

# Set comprehension

s = {s ** 2 for s in [1, 0, 3, 4]}

print(s)


# Generator and yeild -
# Generators do not store elements in memory. They yield one at a time,
# and this behavior makes them memory efficient.
# usecase: 1/ memory use, 2/ infinite iterations and 3/ coroutines.

def data_reader(file_name):
    for row in open(file_name, "r"):
        yield row


# Comprehensive
# csv_gen = (row for row in open(file_name))

# Numeric generator

def oh_dear():
    num = 0
    while True:
        yield num
        num += 1


# Usecase, don't kill anything..
# for i in oh_dear():
#     print(i)

cat_list = ["frank", "jess", "phil"]
# lambda
cat_list = list(map(lambda n: n.title(), cat_list))
print(cat_list)
# Comprehension
cat_list2 = [n.title() for n in cat_list]
print(cat_list2)

# Copy

org = [10,20,30]
copy = org
print(id(copy), id(org), org is copy)

# When you create a slice of a sequence, you actually create a new sequence, this is only going to work on simple sequences (no-nesting)
# To get round this, import copy!

import copy as c
copy = c.deepcopy(org)
print(copy, f"id: {id(copy)}")


# Marks Tutorial
# Maps and Filters

# Map
data = [10,20,30, 3]
dub_data = list(map(lambda i : i*2, data))
print(dub_data)

# Filter
filter_data = list(filter(lambda i : i%2==0, data))
print(filter_data)

# Mini Task
# Cube it!
cube_data = list(map(lambda i : pow(i, 3), data))
print(cube_data)
# Filter cats with names > 3 char
cat_names = list(filter(lambda strn : len(strn) > 3, cat_list))
print(cat_names)


