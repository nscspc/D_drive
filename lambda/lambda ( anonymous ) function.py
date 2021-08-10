#lambda function :-
'''
In Python, an anonymous function is a function that
is defined without a name.While normal functions are
definedusing the def keyword in Python,anonymous
functions are defined using the lambda keyword.Hence,
anonymous functions are also called lambda functions.


Syntax of Lambda Function in python :-

# lambda arguments: expression

Lambda functions can have any number of arguments
but only one expression. The expression is evaluated
and returned. Lambda functions can be used wherever
function objects are required.

'''
# 1 argument :-
x= lambda a : a+10
print(x(5))
print()

# 2 arguments :-
x=lambda a,b:a*b
print(x(5,1))
print()
# more than 2 arguments :-
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

'''
Why Use Lambda Functions?
The power of lambda is better shown when you use
them as an anonymous function inside another function.

Say you have a function definition that takes one argument,
and that argument will be multiplied with an unknown number:

'''
print ()
def mf(n):
    return lambda a : a*n

#calling to double the value :
mydoubler=mf(2)
print(mydoubler(11))

print()

#calling to triple the value :
mytripler=mf(3)
print(mytripler(11))
print( )
# lambda with filter( ) :-
'''
the filter( ) function in python takes in a function and a list as
arguments.

the function is called with all the items in the list and aa new list is
returned which contains items for which the function evaluates to
True.

'''
l=[1,2,3,4,5,6,7,8,9,10,44]
nl=list(filter(lambda x : (x%2==0),l))
print(nl)

print()

nl=filter(lambda x : (x%2==0),l)#in this form it is not readable.
print(nl)
print()

nl=list(filter(lambda x:x,l))
print(nl)

# lambda with map( ) :-
'''
The map() function in Python takes in a function and a list.

The function is called with all the items in the
list and a new list is returned which contains
items returned by that function for each item.

'''
print( )

my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(map(lambda x: x * 2 , my_list))
print(new_list)
print()

new_list = map(lambda x: x * 2 , my_list)#in non-list form it is not readable.
print(new_list)
