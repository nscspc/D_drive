print(isinstance(453,int))

class foo:
    a=5
fooinstance=foo()
print(isinstance(fooinstance,foo))
print(isinstance(fooinstance,(list,tuple)))
print(isinstance(fooinstance,(list,tuple,foo)))
'''
he isinstance() function checks if the object (first argument) is an instance or subclass of classinfo class (second argument).

The syntax of isinstance() is:

isinstance(object, classinfo)
isinstance() Parameters
isinstance() takes two parameters:

object - object to be checked
classinfo - class, type, or tuple of classes and types
Return Value from isinstance()
isinstance() returns:

True if the object is an instance or subclass of a class or any element of the tuple
False otherwise
If classinfo is not a type or tuple of types, a TypeError exception is raised.

Example 1: How isinstance() works?

'''
