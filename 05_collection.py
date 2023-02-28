# Collections

# Tuple
new_tup = "one", "two", "three"
print(type(new_tup))
# Contains or checking values
print(new_tup.count("one"))
# Alias mapping for simplicity
x, y, z = new_tup
print(x, y, z)
# Alias "rest" python version, for wildcard reference
x, *y = new_tup
print(x, y)
# Slicing
print(new_tup[0:len(new_tup)])  # same new_tup[:len(new_tup)]
# Backward slicing
print(new_tup[::-1])
print(new_tup[-2])

# List
new_list = ["one", "two", "three"]
print(type(new_list))
# Add value
# One item
new_list.append("four")
print(new_list)
# Multiple
new_list.extend(["five", "six"])
# Append Right
new_list += ["seven"]
print(new_list)
# Append left
new_list[:0] = ["Zero"]
print(new_list)
# Specific location
new_list[1:1] = ["0.5"]
new_list.insert(2, "0.55")
print(new_list)
# Deleting values
# By position
new_list.pop(1)
print(new_list)
# By value
new_list.remove("Zero")
print(new_list)

# Sets
new_set = {1, 2, 3, 4}
# Unique
new_set.add(1)
print(new_set)
# Add multiple
new_set.update([5, 6, 7])
print(new_set)
# Update set with set
diff_set = {10, 11, 12, 13, 14, 15}
new_set |= diff_set
print(new_set)
# Can also use &= for common element addition and -= to remove different elements
# Removing several values from a list using a set
new_list = list(set(new_list) - {"five", "three", })
print(new_list)

# Dictionary
new_dict = {"one": "value", "two": "value", "three": "value"}
print(type(new_dict))

# print(min(new_dict), max(new_dict)) returns strange results

 # Delete values/pair
del new_dict["one"]
print(new_dict)
# Deletes with a default val if no key present
print(new_dict.pop("four", ["default_val", "check"]))
# Delete in iteration
for i in new_dict.keys():
    # new_dict.popitem()
    print(i)
# Clear the dict
new_dict.clear()
# Dictonary update, works with other dicts
new_dict.update(dict(one="val"))
print(new_dict)
