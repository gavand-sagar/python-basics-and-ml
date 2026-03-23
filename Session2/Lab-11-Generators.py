# numbers = [1,2,3,4,5]

# infinite data

# sequence of all even number

# end???? 

# data = [1,2,3,4,5]

def generator():
    n = 1
    while True:
        n = n + 2
        yield n 

gen_obj = generator()

for i in gen_obj:
    print(i)
    if i >= 5000:
        break

# print(next(gen_obj))
# print(next(gen_obj))
# print(next(gen_obj))
# print(next(gen_obj))
# print(next(gen_obj))
# print(next(gen_obj))
# print(next(gen_obj))
# print(next(gen_obj))
# print(next(gen_obj))
# print(next(gen_obj))

# for s in gen_obj:
#     print(s)