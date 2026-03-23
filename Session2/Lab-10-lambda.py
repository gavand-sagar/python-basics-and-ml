def addition(a, b):
    print(a + b)

add = lambda a, b: print(a + b) # helpful to shorten the code
# but need to be carefull as it will be difficult to debug

print(addition(4, 5))
print(add(4, 5))


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# squares = list(map(lambda x: x * x, numbers))

# print(squares)
