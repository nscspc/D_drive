#python inheritance
'''
inheritance allows us to define a class that inherits all the methods
and properties from another class.

Parent class is the class being inherited from, also called base class.

Child class is the class that inherits from another class, also called
derived class.

'''

#parent class
class parentclass:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def print(self):
        print('hi '+self.name+' , you are '+str(self.age)+' years old')

pc1=parentclass('a',1)
pc1.print()

#child class
class childclass(parentclass):
    pass

cc1=childclass('b',1)
cc1.print()

#child class with some more attributes which are accessible to this particular class only
class child2(childclass):
    def print2(self):#if we are not going to put atleast one parameter in the function defined in the class then while calling(or accessing) the function the 'typeerror' error occurs ,which tells that print2() takes 0 positional argument but 1 was given , because the object-name (c2) in c2.print2() is taken as argument. So it is necessary to mention at least one argument in parenthesis.
        print("this is the child class whose parentclass is the another child class which has an another parent class")

c2=child2('c',1)
c2.print()
c2.print2()

# __init__( ) with child class :
class child3(child2):
    def __init__(self,fname,lname):
        self.name=fname+lname

    def p(self):
        print(self.name)

c4=child3('f','l')
c4.p()

'''
When you add the __init__() function, the child class will no
longer inherit the parent's __init__() function.

Note: The child's __init__() function overrides the inheritance
of the parent's __init__() function.

'''

# To keep the inheritance of the parent's __init__() function , add a call to the parent's __init__() function:
class c5(parentclass):
    def __init__(self,a,b):
        parentclass.__init__(self,a,b)

cc5=c5('2','2')
cc5.print()


