# def sum(*array):
#     result = 0
#     for a in array:
#         result = result + a
#     return result

# # print(sum([3,4,5])) don't want

# print(sum(1,2,3,4,5)) # but this


# def print_user(**kwargs):
#     for key, value in kwargs.items():
#         print(key, value)
#     # print("Name:", name)
#     # print("City:", city)


# print_user(city="Mumbai", name="Sagar", age=56, contact="gavand.sagar.s@gmail.com")


def testFuction(*args, **kwargs):
    print("test")

testFuction(5, 6, 7, 8, 9, 9, 0, city="mumbai")
