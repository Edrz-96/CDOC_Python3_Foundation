a = {1: "a", 2: "b"}

res = dict((v, k) for k, v in a.items())
print(res)

