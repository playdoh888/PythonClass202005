"""
The lambda keyword in Python provides a shortcut for declaring small anonymous functions.

Lambda functions behave just like regular functions declared with the def keyword.
They can be used whenever function objects are required.
"""
add = lambda x, y: x + y

print(add(5, 3))

# You could declare the same add function with the def keyword:
def add(x, y):
    return x + y

print(add(5, 3))

#More examples:

sorted(range(-5, 6), key=lambda x: x ** 2)

