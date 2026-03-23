numbers = [1, 2, 3, 4, 5, 6]

# newArray = [(n + n) for n in numbers]

# print(newArray)

newArray = [(s) for s in numbers if s > 3]  # numbers.where(n=> n > 3).select(n=>n)

print(newArray)
