# Temp converter

# Convert fah to cel
def c_to_f(cel):
    # print((cel * 9 / 5) + 32, "\u2109")
    return (cel * 9 / 5) + 32


# Convert cel to fah
def f_to_c(fah):
    return ((fah - 32) * 5) / 9


c_to_f(100)  # 212
f_to_c(212)  # 100
# Find the unicode characters for Fah and Cel and use these to beautify your output!
print(f_to_c(212), "\u2103")
# Better version...
print(f"{f_to_c(212)}\u2103")
print(f"{c_to_f(100)}\u2109")

if __name__ == '__main__':
    assert f_to_c(212) == 100.0
    assert c_to_f(100) == 212.0
else:
    print("External")
