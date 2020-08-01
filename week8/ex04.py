"""
Multiple-resolution order
if both B and C both had a method with the same name?
This is where a concept called 'multiple-resolution order' comes into play or MRO for short.
The MRO of a child class is what decides where Python will look for a given method,
and which method will be called when there's a conflict.
"""
class B:
    def x(self):
        print('x: B')


class C:
    def x(self):
        print('x: C')


class D(B, C):
    pass


d = D()
print(d.x())
#print(D.mro())

