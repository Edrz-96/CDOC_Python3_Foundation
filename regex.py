import re

# Start with a string, file or other span of text

str = "Wir hab zu viele Zwiebein zum Kochen"

# MetaChar needs handling: . ^ $ * + ? [ ] { } \ | ( )
# e.g. re.compile(r"something/.com")

# .       - Any Character Except New Line
# \d      - Digit (0-9)
# \D      - Not a Digit (0-9)
# \w      - Word Character (a-z, A-Z, 0-9, _)
# \W      - Not a Word Character
# \s      - Whitespace (space, tab, newline)
# \S      - Not Whitespace (space, tab, newline)
#
# \b      - Word Boundary
# \B      - Not a Word Boundary
# ^       - Beginning of a String
# $       - End of a String
#
# []      - Matches Characters in brackets
# [^ ]    - Matches Characters NOT in brackets
# |       - Either Or
# ( )     - Group
#
# Quantifiers:
# *       - 0 or More
# +       - 1 or More
# ?       - 0 or One
# {3}     - Exact Number
# {3,4}   - Range of Numbers (Minimum, Maximum)
#
#
# #### Sample Regexs ####
#
# [a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+


# Email example
# email = "erdz@gotmail.co.uk"
# pattern = re.compile(r"^[\w-.]+@([\w-.]+\.)+[\w-.]{2,4}$")
# match = pattern.finditer(email)
# for m in match:
#     print(m)

# Phone number example
num = "01352-730-730"
primitive_pattern = re.compile(r'\d\d\d\d\d[-.]\d\d\d.\d\d\d')
adv_pattern = re.compile(r'\d{5}[-.]\d{3}[-.]\d{3}[-.]')
match = primitive_pattern.finditer(num)
for m in match:
    print(m)

# File example
next_pattern = re.compile(r"[a-z]")
with open("drop/Errors.txt", "r") as f:
    match = next_pattern.finditer(f.read())
    for m in match:
        print(m)
# Basic search
m = re.search(r"(hab).*(z)", str)
if m:
    print(m.groups(), m.span())
# To understand span, start and end, slice the String with the given chars.
print(str[4:27])

# Expression
line = "change this part of the string"
val1 = re.subn("change", "I will change", line)
print(val1)
# additional predicate will remove count/default value
val1, val2 = re.subn("change", "I will change", line)
print(val1)

# Re split
line = "I will* split: this: string, at certain. points"
print(re.split("[:*.,]", line))

# Alternative matching
pattern = re.compile(r"abc|b|c")
print(re.search(pattern, line))

# Ignore case
print(re.search(r"HAB", str, re.IGNORECASE))



