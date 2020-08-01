"""
3.3. Special method names

A class can implement certain operations that are invoked by special syntax
(such as arithmetic operations or subscripting and slicing) by defining methods with special names.
This is Python’s approach to operator overloading, allowing classes to define their own behavior
with respect to language operators. For instance, if a class defines a method named __getitem__(),
and x is an instance of this class, then x[i] is roughly equivalent to type(x).__getitem__(x, i).
Except where mentioned, attempts to execute an operation raise an exception when no appropriate method
is defined (typically AttributeError or TypeError).

Setting a special method to None indicates that the corresponding operation is not available.
For example, if a class sets __iter__() to None, the class is not iterable, so calling iter()
on its instances will raise a TypeError (without falling back to __getitem__()). 2

When implementing a class that emulates any built-in type, it is important that the emulation
only be implemented to the degree that it makes sense for the object being modelled.
For example, some sequences may work well with retrieval of individual elements,
but extracting a slice may not make sense. (One example of this is the NodeList interface
in the W3C’s Document Object Model.)


"""

class I:

    def __init__(self):
        self.s = 'abc'
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i == len(self.s):
            raise StopIteration

        v = self.s[self.i]
        self.i += 1
        return v

for x in I():

    print(x, end='')


