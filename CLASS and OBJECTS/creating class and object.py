#Python Objects and Classes
'''
Python is an object oriented programming language.
Unlike procedure oriented programming, where the
main emphasis is on functions, object oriented
programming stresses on objects.

An object is simply a collection of data (variables)
and methods (functions) that act on those data.
Similarly, a class is a blueprint for that object.

We can think of class as a sketch (prototype) of a house.
It contains all the details about the floors, doors, windows etc.
Based on these descriptions we build the house.
House is the object.

As many houses can be made from a house's blueprint,
we can create many objects from a class.
An object is also called an instance of a class
and the process of creating this object is called instantiation.

'''
#while working with class / objects :
'''
variables are called attributes.
and
functions are called methods.

'''
# creating a class(blueprint) and object from class :
class myclass:
    x=5#x is an attribute.

#now accessing the class by creating and object :
myobject=myclass()
print(myobject.x)
