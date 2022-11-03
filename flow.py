# As you'd assume, Python has a top-down flow control, this is regulated by conditionals
# transfer or iterative statements.

# Conditional statements
if True:
    print("once")
else:
    print("Twice")

something = "str"
something_else = "str"

if something == something_else:
    print("true")

if "s" in something:
    print("true")
else:
    print("false")

obj_one = str("str")
print(type(obj_one))
print(type("str"))
# Stored at different memory addresses, returns false
print(obj_one is type(" "))
my_list = [1, 2, 3]

# The bool() function returns false on empty lists, tuples, strings, dict and sets additionally, it'll return false
# on None type and 0.

print(bool(0), bool(my_list), bool(None))


# Standard Boolean operators are avialable in Python:
# < > <= >= == != is

# Logical operators
# not and or

# Comparisons can be chained
def return_num(num):
    return num


if return_num(3) < 4 > 2:
    print("something")

# Another great feature of Python is collection tests, where you can check all or any values in a sequence:
if all(my_list):
    print("all are true")

if not any(my_list):
    print("any arent true")
else:
    print("any are true")

# Iteration
# There is no do - while loop in Python
str_in = " "
while str_in != "q":
    str_in = input("type q to quit \n")
    if str_in == "q":
        print("cya")
    else:
        print(str_in)

# Control statements
# pass, continue
i = 1
while i < 5:
    i += 1
    if i > 15:
        break
    else:
        print(f"Looping {i}")

# Enumeration returns a tuple
for n, line in enumerate(open("drop/Errors.txt"), start=1):
    print(n, line, end="")

# Python has a useful function called range(), the main usecase is producing a list of vars quickly.

for i in range(5):
    print(i)

print(my_list)
for i, n in enumerate(my_list):
    if n > 1: my_list[i] += 1
    print(my_list)


list_1 = {1,2,3,4}
list_2 = {1,2,3,4}
list_3 = {1,2,3,4}
list_4 = {1,2,3,4}

for a, b, c, d in zip(list_1, list_2, list_3, list_4): print(a, b, c, d)

# Ternary statement

a = 1
b = 2

1 if a > b else -1
# Output is -1

1 if a > b else -1 if a < b else 0
# Output is -1

