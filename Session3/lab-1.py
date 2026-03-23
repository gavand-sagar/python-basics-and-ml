# class Person:
#     def display(self):
#         print("SOMETHING TO PRINT")
#     def __init__(self):
#         pass

#     def __len__(self):
#         return 10


# p = Person()
# p.display()


# class Number:
#     def __init__(self, value):
#         self.value = value

#     def getValue(self):
#         return self.value

#     def __add__(self, other):  # + operator overloading
#         result = self.getValue() + other.getValue()
#         return Number(result)

#     def __sub__(self, other):  # - operator overloading
#         result = self.getValue() - other.getValue()
#         return Number(result)

#     def __str__(self):
#         return str(self.getValue())


# n1 = Number(40)
# n2 = Number(10)

# result = n1 - n2 + n1

# print(result)


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __getitem__(self, key):
#         if key == "name":
#             return self.name
#         elif key == "age":
#             return self.age
#         else:
#             return None


# p = Person("Tony", 56)

# value = p["name"]

# print(value)


# try:
#     num = int(input("Enter number: "))
#     result = 10 / num

# except ValueError:
#     print("Invalid number")

# except ZeroDivisionError:
#     print("Cannot divide by zero")

# finally:
#     print("Execution finished")


# class AgeException(Exception):  #  AgeException:Exception
#     pass  # to keep the block empty


# try:
#     age = 67

#     if age < 18:
#         raise Exception("must be an adult")  # throw == raise

#     if age > 60:
#         raise Exception("The person is retired")  # throw == raise
# except:
#     pass
# except Exception as ex:
# #     print(ex)
# finally:
#     pass
