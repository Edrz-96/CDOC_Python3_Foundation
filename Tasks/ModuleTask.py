# Since ModuleTask is a task/class I've used PascalCase..

"""This is a module that aims to capture the use of docstrings"""


def func_one(x, y):
    """ This function will add two input parameters together
    >>> func_one(1,2)
    3
    """
    return x + y


if __name__ == "__main__":
    print("Internal")
    # Some simple assertions can be carried out in the if statement.
    # These are ran only if we're running the module from main
    assert func_one(1, 1) == 2
    # We can test our docstrings like so:
    import doctest
    # This will identify methods to test, read the method description by using ctrl + click
    doctest.testmod()
    # The expected answer is defined on the next line after the call and ">>>" keyword
else:
    print("External")





