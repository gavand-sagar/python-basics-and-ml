# Lab 3: For loops and functions – solution

# Python equivalent of for (int i = 0; i < 10; i += 2)
for i in range(0, 10, 2):
    print(i, end=" ")
print()

# Default and keyword arguments
def greet(name, greeting="Hello"):
    return greeting + ", " + name


print(greet("World"))
print(greet("Python", greeting="Hi"))

# Return two values; unpack with a, b = ...
def get_min_max(items):
    return min(items), max(items)


lo, hi = get_min_max([3, 1, 4, 2])
print("min:", lo, "max:", hi)
