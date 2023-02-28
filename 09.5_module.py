# Temperature module

FREEZE = 32


def c_to_f(cel: float) -> float:
    return cel * 9 / 5 + FREEZE


def f_to_c(fah: float) -> float:
    return (fah - FREEZE) * 5 / 9


# Test!
assert f_to_c(212) == 100.0
assert c_to_f(100) == 212.0

# To demo this, copy all but the tests out into another module, or open a new file and import it.
# used to temporarily add a path and as such, that path would be valid for a session for example.
import sys

sys.path.append('./path')
# Check this with sys.path and double check this now has been added!
# If you want to make a perm change, configure the path file.
