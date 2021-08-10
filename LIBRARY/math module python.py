#Python Math
'''
Python has a set of built-in math functions, including
an extensive math module, that allows you to perform
mathematical tasks on numbers.
'''
#Built-in Math Functions
'''
The min() and max() functions can be used to find the
lowest or highest value in an iterable:
'''
x = min(5, 10, 25)
y = max(5, 10, 25)
print(x)
print(y)
print( )

'''
The abs() function returns the absolute (positive) value
of the specified number:
'''
x = abs(-7.25)
print(x)
print( )

'''
The pow(x, y) function returns the value of x to the
power of y (xy).
'''
x = pow(4, 3)
print(x)
print( )

#The Math Module
'''
Python has also a built-in module called math,
which extends the list of mathematical functions.

To use it, you must import the math module:
'''
import math
x = math.sqrt(64)
print(x)
print( )

'''
The math.ceil() method rounds a number upwards to
its nearest integer, and the math.floor() method
rounds a number downwards to its nearest integer,
and returns the result:

'''
import math

x = math.ceil(1.4)
y = math.floor(1.4)

print(x) # returns 2
print(y) # returns 1
print( )

'''
The math.pi constant, returns the value of PI (3.14...):
'''
import math
x = math.pi
print(x)
print( )
