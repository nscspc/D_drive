# __init__( ) :-
'''
All classes have a function called __init__( ) , which is always executed
when the class is being initiated.

There should be double underscore .

'''
class person:
    def __init__(self,name,age):
        self.name=name# __init( )__ function is normally used to initialize the variables.
        self.age=age

p1=person("john",36)
print(p1.name)
print(p1.age)
# print(p1.k) #attribute error ; As person class has no attribute 'k'.
'''
 The __init__() function is called automatically
 every time the class is being used to create a new object.

'''
