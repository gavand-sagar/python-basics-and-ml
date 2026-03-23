# Lab 2: Variable declaration and dynamism – solution

# No explicit types; same name can hold different types
x = 10
print("x =", x, "→ type:", type(x).__name__)

x = "hi"
print("x =", x, "→ type:", type(x).__name__)

# PEP 8: snake_case for variables
user_name = "Alice"
item_count = 42

# Variables are references to objects
a = [1, 2]
b = a
a.append(3)
print("a =", a, "b =", b)  # same list
