# Lab 5: Classes and objects – solution

class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return "Hi, " + self.name


# No "new" keyword
p = Person("Alice")
print(p.greet())
