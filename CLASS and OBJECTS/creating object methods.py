# Object Methods :-
'''
Objects can also contain methods . Methods in objects are
functions that belong to the object .

'''
class person:
    def __init__(notself,name,age):
        notself.name=name
        notself.age=age

    def mf(another):
        print("hello my name is "+another.name)

p1=person("john",36)
p1.mf()

'''
The self parameter is a reference to the current instance
of the class, and is used to access variables that belong
to the class.

It does not have to be named self , you can call it
whatever you like, but it has to be the first
parameter of any function in the class:

it is not necessary to write first parameter of the methods
as ' self ' , we can use any word as parameter but not keywords.

'''
