'''
Like function definitions begin with the def keyword in
Python, class definitions begin with a class keyword.

The first string inside the class is called docstring and
has a brief description about the class.
Although not mandatory, this is highly recommended.

A class creates a new local namespace where all its
attributes are defined. Attributes may be data or functions.

There are also special attributes in it that begins
with double underscores __. For example, __doc__
gives us the docstring of that class.

As soon as we define a class, a new class object is created
with the same name. This class object allows us to access
the different attributes as well as to instantiate
new objects of that class.

'''

class person:
    "this is a person class"
    age=10

    def greet(self):
        print("hello")

print(person.age)
print()
print(person.greet)
print()
#person.greet()
print()
print(person.__doc__)
