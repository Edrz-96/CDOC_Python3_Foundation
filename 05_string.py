# Strings in Python 3 are unicode
# Multi-byte characters
# \unnnn for a two-byte Unicode character
# \Unnnnnnnn for a four-byte Unicode character
# \N{name} for a named Unicode character

import sys as s

my_str = "hello world"
my_str_as_bytes = str.encode(my_str)
print(type(my_str_as_bytes))  # ensure it is byte representation
my_decoded_str = my_str_as_bytes.decode()
print(type(my_decoded_str))  # ensure it is string representation

# The print function
# End=
print("Print this ", end=" ")
list_str = "this is a list"
new_list = list_str.split(" ")

# Sep=
print(new_list, str("new string"), sep=", ")

# File=
print("This will print as red error text!", file=s.stderr)

with open('Files/Errors.txt', 'w') as f:
    print('This message will be written to a file.', file=f)
    print('This message will be written to a file.', file=f)
# Flush=
print("Reset the os buffer", flush=True)

# String concatenation
user = "Ed" \
       "Reynolds"
first_name = "Ed"
last_name = "Reynolds"

user = first_name + last_name
print(user)

# You might hear that String are immuateable, whilst true, you can change where a variable points, so it's
# perfectly valid to update user.
user = "{} {}".format(first_name, last_name)
print(user)

# Here we'll prove Strings are immutable:
str_a = "test"
str_b = str_a

print(str_a, str_b, sep=" ")

str_a = "updated"
print(str_a, str_b, sep=" ")
# An even better example
# str_a[0] = "1", this will fail

# String formatting
# https://www.w3schools.com/python/ref_string_format.asp
# Old style:
print("Hey, %s" % user)
# Where %s is String, %d is numbers, %x is hex and so on..

# New style:
new_str = "this is a {} string".format("new")
print(new_str)

# We can specify index, width and rounding too:
new_str = "index 0 {0} and rounding {1:5.3f}"

# Template literals
# Syntax is {value:{width}.{precision}}
print(f"Hey, {user}")
print(f"Hey, {user:<5s}, {str_a:2s}")
#
# planets = {'Mercury': 57.91,
#            'Venus': 108.2,
#            'Earth': 149.597870,
#            'Mars': 227.94
#            }
# for i, key in enumerate(planets.keys(), 1):
#     print("{:2d} {:<10s} {:06.2f} Gm".
#           format(i, key, planets[key]))

# Additional formatting
new_text = "text"
new_num = str(1)
print(new_text.capitalize())
print(new_text.lower())
print(new_num.zfill(2))
print(new_text.title())

# String slicing
print(new_text[:3])  # Forward
print(new_text[3:])  # Backward
print(new_text[0:2])
print(new_text[0:4:2])  # Every 2 chars
print(new_text[::-1])

# String join and splitting
string = "this is a string with, commas in it, not ideal.."
print(string.split(","))
print(string.split(",", 1))
# .join() with tuples
separator = " "
numTuple = ('1', '2', '3', '4')
print(separator.join(numTuple))

# opening the file
file = open("Files/Errors.txt", "r")

# reading the data from the file
file_data = file.read()

# splitting the file data into lines
lines = file_data.splitlines()
print(lines)
file.close()

with open("Files/Errors.txt", "r") as f:
    for i in f:
        print(i, end="")

# Additional String formatting examples
dict_user = {"name": "Ed", "hands": 2}
dict_str = "{}, has {} hands..!".format(dict_user["name"], dict_user["hands"])  # Can be explict with index
dict_str = "{0[name]}, has {0[hands]} hands..!".format(dict_user)
print(dict_str)

# f String
# {n:02} zero value padding in this example n = 0n
# {n:.3} sets decimal point limit to three
# {n:3.3} sets the minimum field width including the decimal to 3


print('{0:#x}'.format(1))
print('{0:06}'.format(1))
print("{:06.2f}".format(12))

euro = "\N{euro sign}"
