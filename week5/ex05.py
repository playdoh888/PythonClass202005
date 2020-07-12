"""
Given  a list of integers and we want to square each element of the list using the map function.
"""

L = [1, 2, 3, 4]

result = map(lambda x: x**2, L)
print(list(result))


# def myfunc(n):
#     return len(n)
#
# x = map(myfunc, ('apple', 'banana', 'cherry'))

