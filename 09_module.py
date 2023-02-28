# What is a module..

# Create new directory, add __init__.py to turn the dir into a package
# After this add __all__ = [list of module], giving us the ability to call * on imports.
# Additionally, adding "from mod import func" is a best practice tech

# Adding documentation to a module is quite simple, within """ Add some documentation""", when this is on the funciton
# scope, your docstring is for the function!
# e.g. mymodule.__doc__


#pydoc
# Generates html documentation based on the code, however, if you don't document you get nothing!

# PYC, PYD, etc..
# pyc
# Files of type .pyc are automatically generated by the interpreter when you import a module, generally, this speeds
# up future imports.
# What this means is that you can improve startup time by writing your main program
# in a module that gets imported by another, smaller module.
# To avoid bugs, adding .pyc files to your ignore VC list is ideal. This is because updates to source code wont
# be reflected in bytecode.
# pyd
# The pyd file, specific to Windows, simply put; it's a file that contains Python code!
# (DLLs) are Windows code libraries that are linked to calling programs at run time.
# The main advantage of linking to libraries at run time is the same as the above, it facilitates code reuse,
# modular architectures and faster program startup.

# doctest

# Import the doctest module.
# Write the function with docstring.
# Inside the docstring, write the following lines for testing of the same function.
# Write the function code.
# Now, call the doctest.testmod(name=function_name, verbose=True) function for testing.
# E.G.
# """>>> func_name(1, 2, 3)
# 6
# doctest.testmod(name="func_name", verbose=True)

## pbd - debugging
# When invoked as a script, pdb will automatically enter  post-mortem debugging
# if the program being debugged exits abnormally.
# Ran from CLI python3 -m pdb myscript.py
# Ran from script:
# import pdb
# import mymodule
# pdb.run('mymodule.test()')
