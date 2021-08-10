#Python Custom Module :-
'''
What is a Module?
Consider a module to be the same as a code library.

A file containing a set of functions you want to
include in your application.

'''
#Create a Module
'''
To create a module just save the code you want
in a file with the file extension .py:

Example
Save this code in a file named mymodule.py

'''
def greeting(name):
  print("Hello, " + name)

# Using a Module :-
'''
we can use the module that we have created by using
'import' statement .

code => import mymodule
      => mymodule.greeting('jonathan')

when using a function from a module use the syntax :-
    => module_name.function_name( )

'''
# Variable in module :-
'''
the module can contain functions , and also variables of all types
( arrays , dictionary , objects  etc ) .

save the code in the file mymodule.py :

code  => person={
                    "name":"john"
                    "age":36
                    "country":"norway"
                    }

code  => import mymodule
            a=mymodule.person["age"]
            print(a)

'''

# Naming a Module
'''
You can name the module file whatever you like, but it
must have the file extension .py

'''
# Re-naming a Module
'''
You can create an alias when you import a module, by
using the as keyword:

Example
Create an alias for mymodule called mx:

code => import mymodule as mx
            a = mx.person1["age"]
            print(a)

'''
# Built - in Modules :-
'''
platform => the platform module in python is used to access the
                underlying platform's data , such as hardware,
                operating system , and interpreter version
                information , system , and interpreter version
                information where the program is running .

'''
import platform
print(platform . system( ))#os.
print(platform . processor( ))#processor information.
print(platform . architecture( ))# bit(32,64) information.
print(platform . machine( ))#amd .
print(platform . node( ))#name of system=Mylapi.
print(platform . platform( ))#os full information.
print(platform . python_build( ))#whole information when python was installed.
print(platform . python_compiler( ))#compiler information.
print(platform . python_version( ))#version of  python.
print(platform . python_implementation( ))#cpython.

# dir( ) function :-
'''
this function is used to list all the functions names or
variables names in a module

'''
import platform
x=dir(platform)
print(x)

'''
the dir( ) function can be used on all modules , also the
ones you create youself .

'''

# Import From Module
'''
You can choose to import only parts from a module,
by using the from keyword.

'''
def greeting(name):
  print("Hello, " + name)

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}
'''
Import only the person1 dictionary from the module:

from mymodule import person1

print (person1["age"])
'''
