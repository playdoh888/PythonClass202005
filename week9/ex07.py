"""
Usage of *args
*args and **kwargs are mostly used in function definitions. *args and **kwargs allow you to pass a variable number of arguments to a function.
What variable means here is that you do not know beforehand how many arguments can be passed to your function
by the user so in this case you use these two keywords. *args is used to send a non-keyworded variable length argument list to the function.
Here’s an example to help you get a clear idea:
"""


def test_var_args(f_arg, *argv):
    print("first normal arg:", f_arg)
    for arg in argv:
        print("another arg through *argv:", arg)


test_var_args('yasoob', 'python', 'eggs', 'test')

"""
Usage of **kwargs
**kwargs allows you to pass keyworded variable length of arguments to a function. 
You should use **kwargs if you want to handle named arguments in a function. 
Here is an example to get you going with it:
"""


def greet_me(**kwargs):
    for key, value in kwargs.items():
        print("{0} = {1}".format(key, value))


greet_me(name="yasoob")

"""
Using *args and **kwargs to call a function
So here we will see how to call a function using *args and **kwargs. 
Just consider that you have this little function:
"""


def test_args_kwargs(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)

print("\nPrint out of \"args\"")
args = ("two", 3, 5)
test_args_kwargs(*args)

print("\nPrint out of \"kwargs\"")
kwargs = {"arg3": 3, "arg2": "two", "arg1": 5}
test_args_kwargs(**kwargs)

"""
Order of using *args **kwargs and formal args

So if you want to use all three of these in functions then the order is

some_func(fargs, *args, **kwargs)
"""
