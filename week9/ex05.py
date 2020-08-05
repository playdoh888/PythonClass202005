"""
Functions and methods are called callable as they can be called.

In fact, any object which implements the special __call__() method is termed callable.
So, in the most basic sense, a decorator is a callable that returns a callable.

Basically, a decorator takes in a function, adds some functionality and returns it.

"""


def make_pretty(func):
    def inner():
        print("I got decorated")
        func()

    return inner


def ordinary():
    print("I am ordinary")


ordinary()
pretty = make_pretty(ordinary)  # We decorate a function and reassign it as,
pretty()

"""
We can see that the decorator function added some new functionality to the original function. 
This is similar to packing a gift. The decorator acts as a wrapper. 
The nature of the object that got decorated (actual gift inside) does not alter. 
But now, it looks pretty (since it got decorated).

This is a common construct and for this reason, Python has a syntax to simplify this.

We can use the @ symbol along with the name of the decorator function 
and place it above the definition of the function to be decorated. For example,

"""


@make_pretty
def ordinary():
    print("I am ordinary")

#
# is equivalent to
# def ordinary():
#     print("I am ordinary")
# ordinary = make_pretty(ordinary)
#
