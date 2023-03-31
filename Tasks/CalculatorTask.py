# User input
num_one = int(input("Enter a number"))
num_two = int(input("Enter a number"))


# Calculator
def add(x: int, y: int) -> int:
    return x + y


def mul(x: int, y: int) -> int:
    return x * y


def div(x: int, y: int) -> float:
    return x / y


def sub(x: int, y: int) -> int:
    return x - y


# Menu
def menu():
    end = False
    while not end:
        selection = input("Please input an option, add, sub, div or mul. To exit out of the calculator, please type q")
        match selection:
            case 'add':
                print(add(num_one, num_two))
            case 'sub':
                print(sub(num_one, num_two))
            case 'div':
                print(div(num_one, num_two))
            case 'mul':
                print(mul(num_one, num_two))
            case 'q':
                end = True
                print("Goodbye!")
            case other:
                print("That is selection is not correct..!")


menu()
