"""
Class objects support two kinds of operations: attribute references and instantiation.

Generally speaking, instance variables are for data unique to each instance and
class variables are for attributes and methods shared by all instances of the class:
"""

class A:
    X = 0
    def __init__(self, v = 0):
        self.Y = v
        A.X += v

a = A()
b = A(1)
c = A(2)

print(c.X)

class Dog:

    kind = 'canine'         # class variable shared by all instances

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance

d = Dog('Fido')
e = Dog('Buddy')
print(d.name)
print(d.kind)
print(e.name)
print(e.kind)

class SmartDog:

    tricks = []             # mistaken use of a class variable

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)

d = SmartDog('Fido')
e = SmartDog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
print(d.tricks)
print(e.tricks)
