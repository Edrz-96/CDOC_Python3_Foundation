def outer(func):
    def wrapper():
        print("before")
        func()
        print("after")

    return wrapper


def print_mid():
    print("middle")


print_now = outer(print_mid)

print_now()


def print_twice(func):
    def wrapper(*var, **kwargs):
        func(*var, **kwargs)
        func(*var, **kwargs)

    return wrapper


@print_twice
def print_it_now():
    print("hey")


print_it_now()
