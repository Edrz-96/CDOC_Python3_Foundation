import os.path
import sys
import traceback

# In theory, you have two methods of handling exceptions: LBYL, EAFP. Now, there is an element of context to these
# strategies. However, the two methods can be broken down into a file handling example.
# You shouldn't error handle unless you know what error you're trying to catch!

file_works = False
### EAF ###
while not file_works:
    try:
        file_name = input("Enter name of file")
        file = open(file_name, end="")
    except FileNotFoundError as err:
        traceback.print_tb(err.__traceback__)
    else:
        for i in file:
            print(i)
        file.close()
    # Best example of finally is when used in a function, to close down or stop processes that would be ignored
    # by the error!
    finally:
        print("End")

### LBYL ###
if os.path.exists(file_name):
    file = open(file_name, "rt")

# Try blocks intro
try:
    # Throw your own error
    raise Exception
except Exception:
    print("Error!!")
    print("File not found!")
else:
    print("Code to run after try")
finally:
    print("Ran last!")

# Multiple exceptions

try:
    file = open("FileNotFound.txt")
except FileNotFoundError as fe:
    print("File not found!", fe)
except Exception as e:
    print("General error", e)
else:
    file.read()
    file.close()
    print("Code to run after try")
finally:
    print("Ran last!")

# Flow control statements

# Break - breaks out of the flow

# Continue - continues flow

# Pass - skips

# Warnings

import warnings


def warn():
    warnings.warn("deprecated", DeprecationWarning)


with warnings.catch_warnings(record=True) as w:
    # Cause all warnings to always be triggered.
    warnings.simplefilter("always")
    # warnings.simplefilter("error")

    # Trigger a warning.
    warn()
    # Verify some things
    assert "deprecated" in str(w[-1].message)


# Assert

def my_func(*arguments):
    assert any(arguments), 'False argument in my_func'
    # When ran from cli -o will ignore asserts


my_func('Tom', '', 42)


# Raise
def my_func(*arguments):
    if not all(arguments):
        raise ValueError('False argument in my_func')


try:
    my_func('Tom', '', 42)
except ValueError as err:
    print('Oops:', err, file=sys.stderr)


# Creating our own exceptions
class RaiseError(Exception):
    pass


# Traceback
try:
    open("some file name")
except FileNotFoundError as err:
    tipe, val, tb = sys.exc_info()
print("Exception lineno:", tb.tb_lineno, tipe, val)

# traceback.print_tb(e.__traceback__)
