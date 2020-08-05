"""
Decorating Functions with Parameters
The above decorator was simple and it only worked with functions that did not have any parameters.
What if we had functions that took in parameters like:
"""


def divide(a, b):
    return a / b


print(divide(2, 5))


# print(divide(2, 0))


def smart_divide(func):
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("Whoops! cannot divide")
            return

        return func(a, b)

    return inner


@smart_divide
def divide(a, b):
    print(a / b)


print(divide(2, 5))
print(divide(2, 0))


@smart_divide
def subtract(a, b, c):
    print(a - b - c)


# print("What about a function that takes 3 parameters? ")
# print(subtract(2, 3, 9))

def works_for_all(func):
    def inner(*args, **kwargs):
        print("I can decorate any function")
        return func(*args, **kwargs)

    return inner


@works_for_all
def subtract(a, b, c):
    print(a - b - c)


print("Try it again with *args and **kwargs. What about a function that takes 3 parameters? ")
subtract(2, 3, 9)

"""
Chaining Decorators in Python
Multiple decorators can be chained in Python.

This is to say, a function can be decorated multiple times with different (or same) decorators. 
We simply place the decorators above the desired function.
"""


def star(func):
    def starinner(*args, **kwargs):  # First gets called
        print("*" * 30)
        func(*args, **kwargs)  # call the
        # @percent
        # def printer(msg):
        #     print(msg)
        print("*" * 30)

    return starinner


def percent(func):
    def percentinner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)  # call
        # def printer(msg):
        #     print(msg)
        print("%" * 30)

    return percentinner


@star
@percent
def printer(msg):
    print(msg)


printer("Hello")


# The same as:
def printer(msg):
    print(msg)


print("\nJust function no decorator...")
printer = star(percent(printer))

printer("Same Hello?")