# There are many benefits of using Python as a programming language:

# Free-to-use - It is open-source and freely distributable, which also means it has a massive community behind it.
# Beginner-friendly - It is designed to be easy to read and learn, making it easy to understand as a first language.
# Extensible - It has over 200,000 packages available for installation, providing additional functionality to your programs.

# There are also many drawbacks to using Python over other languages:

# Slow speed - Due to being an interpreted and dynamically-typed language, it is much slower than many other languages.
# Memory intensive - Its objects are generally very inefficient in memory usage, making it important to keep track of memory usage in a project.
# Dynamically-typed - Many consider this to be an advantage, as it improves flexibility, but others would rather know the type any variable will be throughout runtime.


def run():
    print("Running from main!")


def external():
    print("Ran from import")


if __name__ == '__main__':
    run()
else:
    external()
