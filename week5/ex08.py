"""
Ways to Pass Arguments

Like a normal function, a lambda function supports all the different ways of passing arguments.
This includes:

    Positional arguments
    Keyword arguments
    Default argument
    Variable list of arguments (*args)
    Variable list of keyword arguments (**args)
"""
# Positional arguments
add = lambda x, y, z: x+y+z
print(add(2, 3, 4))
# Prints 9

# Keyword arguments
add = lambda x, y, z: x+y+z
print(add(2, z=3, y=4))
# Prints 9

# Default arguments
add = lambda x, y=3, z=4: x+y+z
print(add(2))
# Prints 9

# *args
add = lambda *args: sum(args)
print(add(2, 3, 4))
# Prints 9

def myfunc(n):
  return len(n)

# **args
add = lambda **kwargs: sum(kwargs.values())
print(add(x=2, y=3, z=4))
# Prints 9

# **args
add = lambda **kwargs: myfunc(kwargs.values())
print(add(x="apple", y="banana", z="cherry"))

