"""
* Generators in Python
There is a lot of work in building an iterator in Python. We have to implement a class
with __iter__() and __next__() method, keep track of internal states,
and raise StopIteration when there are no values to be returned.

This is both lengthy and counterintuitive. Generator comes to the rescue in such situations.

Python generators are a simple way of creating iterators.
All the work we mentioned above are automatically handled by generators in Python.

Simply speaking, a generator is a function that returns an object (iterator)
which we can iterate over (one value at a time).

* What is Python yield?
The yield keyword in python works like a return with the only

difference is that instead of returning a value, it gives back a generator object to the caller.

When a function is called and the thread of execution finds a yield keyword in the function,
the function execution stops at that line itself and it returns a generator object

"""


# A simple generator function
def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n


a = my_gen()
print(next(a))

print(next(a))

print(next(a))

# print(next(a))

"""
One interesting thing to note in the above example is that the value of 
variable n is remembered between each call.

Unlike normal functions, the local variables are not destroyed when the function yields. 
Furthermore, the generator object can be iterated only once.

To restart the process we need to create another generator object using something 
like a = my_gen().

"""
a = my_gen()
print(next(a))

"""
One final thing to note is that we can use generators with for loops directly.

This is because a for loop takes an iterator and iterates over it using next() function. 
It automatically ends when StopIteration is raised.
"""
print("\n\"for loop\" with Generator... ")
for item in my_gen():
    print(item)
