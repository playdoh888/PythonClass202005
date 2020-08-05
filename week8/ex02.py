"""
._variable is semiprivate and meant just for convention

.__variable is often incorrectly considered superprivate,
while it's actual meaning is just to namemangle to prevent accidental access[1]

.__variable__ is typically reserved for builtin methods or variables
"""

class A:
    def __init__(self,v):
        self.__a = v + 1
        self._b = v + 1

    def get_a(self):
        return self.__a

a = A(0)
print(a._b)
#print(a.__a)
print(a.get_a())


class MyClass():
    def __init__(self):
        self.__superprivate = "Hello"
        self._semiprivate = "world"

mc = MyClass()
print(mc._semiprivate)
print(mc.__superprivate)

