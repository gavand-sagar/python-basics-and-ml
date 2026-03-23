# Lab 4: Arrays in Python – solution

# Every second element: slicing vs loop
lst : list[int] = [10, 20, 30, 40, 50, 60]
every_second_slice = lst[::2]
print("Slicing lst[::2]:", every_second_slice)

every_second_loop = [lst[i] for i in range(0, len(lst), 2)]
print("Loop:", every_second_loop)

# String slicing
s = "hello"
print("s[1:4] =", s[1:4])
print("s[::-1] =", s[::-1])

# Tuple, dict, set
t= (1, 2, 3)
d = {"a": 1, "b": 2}
st = {1, 2, 2, 3}

print("tuple t[0]:", t[0])
print("dict d['a']:", d["a"])
print("set (no duplicates):", st)
