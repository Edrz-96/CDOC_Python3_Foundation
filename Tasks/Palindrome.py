import trace


def solution_one():
    text = input("Enter text")
    if text == text[::-1]:
        print("Input is palindrome")
    else:
        print("Input isn't a palindrome")


def solution_two():
    text = input("Enter text")
    text_for_func = text.split(" ")
    text_for_join = "".join(text_for_func)
    if text_for_join == text_for_join[::-1]:
        print("Input is palindrome")
    else:
        print("Input isn't a palindrome")


def solution_three():
    text = input("Enter text")
    text_for_join = text.replace(" ", "")
    print(text_for_join)
    if text_for_join == text_for_join[::-1]:
        print("Input is palindrome")
    else:
        print("Input isn't a palindrome")


if __name__ == '__main__':
    solution_one()
    solution_two()
    solution_three()
