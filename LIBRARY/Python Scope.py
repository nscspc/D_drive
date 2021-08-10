# Python Scope
'''
A variable is only available from inside the region it is created. This is called scope.
'''
#Function Inside Function
'''
As explained in the example above, the variable x is not available
outside the function, but it is available for any function inside the function:

'''
def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()

# Global Scope
'''
A variable created in the main body of the Python code is a global
variable and belongs to the global scope.

Global variables are available from within any scope, global and local.

'''
x = 300

def myfunc():
  print(x)

myfunc()

print(x)

# Naming Variables
'''
If you operate with the same variable name inside and outside
of a function, Python will treat them as two separate variables,
one available in the global scope (outside the function) and one
available in the local scope (inside the function):

'''

x = 300

def myfunc():
  x = 200
  print(x)

myfunc()

print(x)

# global keyword :-
'''
if we need to create a global variable , but stuck in the local
scope , we can use the global keyword.

the global keyword makes the variable global.

'''
def f( ):
    global x
    x=400

f( )
print(x)

'''
global keyword should also be used while making change to a
global variable inside a function .

'''

x=300
def fn( ):
    global x
    x=200

fn( )
print(x)
