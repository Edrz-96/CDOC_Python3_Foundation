# Like other programming languages Python has set datatypes, however, given Python is dynamically typed,
# there are a few ways to declare and use variables see below:


# Strings in Python is "str", strings have many methods allowing us to handle strings in a verity of ways.
name = "Steve"
name_two = "Steve " "Jones"
nameFour = "check {}".format("this works")
nameThree = str("Steve")
name_five = "Steve " + "Jones"

# Boolean
discount = False

# Numeric Types
# Int
age = 32
# Float
wallet = 29.95

#Long


# Complex
c = 3 + 3j
a = complex(2, -1)
# Additional libaries: SkiDL, PySpice, Numpy ...etc

# Binary


# Sequence#
# Lists
new_list = ["one", "two"]
print(type(new_list))
# Tuples are essentially a read-only list in that you can read the data in exactly the same way,
# you just can't change the data once the tuple has been defined. This characteristic is known as immutability.
new_tuple = "perm_value", "perm_value_two"
print(type(new_tuple))
# Unpacking tuples:
new_pack = "value", "balue", "ealue"
value_one, value_two, value_three = new_pack
print(value_one)

# Sets are unordered, and so we cannot index items within them in any way.
# Sets cannot contain duplicate values, similar to the keys in a dictionary.
# Sets cannot contain other sets, so we can never have a multi-dimensional set.

new_set = {1, 2, 3, 4}
print(type(new_set))
new_items = ["Apple", "Banana", "Apple", "Banana", "Orange"]
set(new_items)  # duplication gone!

# Mapping
new_dict = {1: "Value", 2: "Value", 3: ["Value", "Value", "Value"]}
for key, value in new_dict.items():
    print(key, value)

print("\n")

for i in new_dict.keys():
    print(i, new_dict[i])

print("\n")

for j in new_dict.keys():
    print("key: {} value: {}".format(j, new_dict[j]))
