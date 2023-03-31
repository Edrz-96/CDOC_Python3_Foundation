# Create a set of functions or function that checks if a given string is a palindrome
# Here are your strings to test:
# Check one:'racecar'
# Check two: 'A nut for a jar of tuna.'
# Check three: 'A Man, a Plan, a Canal, Panama.'


def check_one(word):
    print(f"{word} is palindrome!") if word == word[::-1] else print(f"{word} isn't palindrome!")


def check_one_two(word):
    return True if word == word[::-1] else False


def check_two(word: str):
    print(f"{word} is palindrome!") if word.lower().replace('.', "").replace(" ", "") == word[::-1].lower() \
        .replace('.', "").replace(" ", "") else print(f"{word} isn't palindrome!")


check_two("A nut for a jar of tuna.")


def check_three(word: str):
    text = word.lower()
    text = text.replace(" ", "").replace(".", "").replace(",", "")
    return text == text[::-1]


# adv method with regex #
import re


def check_three_re(word):
    text = re.sub(r'[,.\s]', "", word)
    text = text.lower()
    return text == text[::-1]


print(check_three("A Man, a Plan, a Canal, Panama."))
