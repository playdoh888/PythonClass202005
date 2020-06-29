"""
Using lambdas with list sorting
"""

# Sorting a List of Numbers
# list.sort(reverse=True)
# Sort with custom function using key:
#   If you want your own implementation for sorting,
#   the sort() method also accepts a key function as an optional parameter.
#
# Based on the results of the key function, you can sort the given list.
L = [15, 22.4, 8, 10, 3.14]
L.sort()
print(L)

# to create a new sorted list without modifying the original one,
# you should use the sorted function instead
L = [15, 22.4, 8, 10, 3.14]
sorted_list = sorted(L)
print(f'L: {L}')
print(f'sorted_list: {sorted_list}')

# Sometimes you have a list of custom objects and
# you want to sort the list based on a specific object field.

class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

Alex = Employee('Alex', 20)
Amanda = Employee('Amanda', 30)
David = Employee('David', 15)

L = [Alex, Amanda, David]

# We want to sort this list based on the age of the employees
L.sort(key=lambda x: x.age)
print([item.name for item in L])
