"""
The dir() function returns all properties and methods of the specified object, without the values.

This function will return all the properties and methods, even built-in properties which are default for all object.
If the object has a method named __dir__(), this method will be called and must return the list of attributes.
This allows objects that implement a custom __getattr__() or __getattribute__() function to customize
the way dir() reports their attributes.

If the object does not provide __dir__(), the function tries its best to gather information
from the object’s __dict__ attribute, if defined, and from its type object.
The resulting list is not necessarily complete,
and may be inaccurate when the object has a custom __getattr__().
"""
import inspect

class Hello():
    pass


jack = Hello()

print(inspect.getmembers(jack, predicate=inspect.isfunction))

print (dir(jack))



