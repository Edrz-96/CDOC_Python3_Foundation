# A person travels using their personal car.
# They're paid an allowance based on the mules travelled and the engine size of their car.
#
# Basic rate is 0.15p pm for engines less than 1.3L
#
# Other engines award 0.25p per pm.
#
# Calculate and output the allowance for a given person.
#
# Two solutions:
car = float(input("Enter the engine size of your car"))
res_dict = {"Y": 0.15, "N": 0.25}


# 1. If statement
def with_if(engine_size, miles):
    if engine_size < 1.3:
        return 0.15 * miles
    else:
        return 0.23 * miles


# 2. No if statements
def no_if(engine_size, miles):
    while engine_size < 1.3:
        return 0.15 * miles
    else:
        return 0.23 * miles


def no_if_two(miles):
    return res_dict.get(input("Is your engine smaller than 1.3L? Please answer with Y or N").upper())*miles


print(f"£{no_if(car, 20)}")
print(f"£{with_if(car, 20)}")
print(no_if_two(20))
