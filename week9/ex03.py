def first(msg):
    print(msg)


first("Hello")

second = first
second("Hello")

"""
Functions can be passed as arguments to another function.

If you have used functions like map, filter and reduce in Python, 
then you already know about this.

Such functions that take other functions as arguments are also called higher order functions. 
Here is an example of such a function.
"""


def inc(x):
    return x + 1


def dec(x):
    return x - 1


def operate(func, x):
    result = func(x)
    return result


print(operate(inc, 3))
print(operate(dec, 3))

"""
Furthermore, a function can return another function.
"""


def is_called():
    def is_returned():
        print("Let me return a \"Hello\"")

    return is_returned


new = is_called()
new()

