
import re

# pcre.sub(r'def')
# //([\p{L}'])*([\p{L}]|\w)@\w+(\.[A-Z|a-z]{2,})+
# Start with a string, file or other span of text

str = "Wir hab zu viele Zwiebein zum Kochen"


# MetaChar needs handling: . ^ $ * + ? [ ] { } \ | ( )
# e.g. re.compile(r"something/.com")
# email in any language: ([\p{L}'])*([\p{L}]|\w)@\w+(\.[A-Z|a-z]{2,})+
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

# Help funcs

def read(file):
    for i in file:
        print(i)


def match_ite(pat, var_to_match):
    for i in pat.finditer(var_to_match):
        print(i)


# Email example
email = "erdz@gotmail.co.uk"
match_email = re.compile("([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+")
match = match_email.finditer(email)
for m in match:
    print(f"email matched: {m}")

# Phone number example
num = "01352-730-730"

primitive_pattern = re.compile(r'\d\d\d\d\d[-.]\d\d\d.\d\d\d')
adv_pattern = re.compile(r'\d{5}[-.]\d{3}[-.]\d{3}[-.]')
mob_num_pattern = re.compile(r'\d{11}')

print("test")
match_ite(primitive_pattern, num)

# File example

with open("Files/amalg.txt", "r") as f:
    match = mob_num_pattern.finditer(f.read())
    for m in match:
        n = open("Files/numbers.txt", "w")
        print(m)
        n.write(m.string)

num_file = open("Files/numbers.txt", "r")
read(num_file)

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
val2 = re.sub("change", "I will change", line)
print(type(val2))
# additional predicate will remove count/default value
val1, val2 = re.subn("change", "I will change", line)
print(val1, val2)
print(type(val1))

# Re split
line = "I will* split: this: string, at certain. points"
print(re.split("[:*.,]", line))

# Alternative matching
pattern = re.compile(r"abc|b|c")
print(re.search(pattern, line))

# Ignore case
print(re.search(r"HAB", str, re.IGNORECASE))




