# Decorators in Python :-
'''
=> Decorators are very powerful and useful tool in python since it allows
    programmers to modify the behaviour of function or class.
=> Decorators allow us to wrap another function in order to extend the
    behaviour of the wrapped function,without permanently modifying it.
'''
# First Class Objects :- What is a first class object in programming?
'''
=> A first class object is an entity that can be dynamically created,
    destroyed, passed to a function, returned as a value, and have all
    the rights as other variables in the programming language have.

=> In Python ji , functions are first class objects that means that
    functions in python can be used or passed as arguments.

=> Properties of first class functions:
    -> A function is an instance of the Object type.
    -> You can store the function in a variable.
    -> You can pass the function as a parameter to another function.
    -> You can return the function from a function.
    -> You can store them in data structures such as hash tables, lists, …

'''
#----------------------------------------------------

# Treating the functions as objects:-

def shout(text):
    return text.upper()

print(shout("hello"))

yell=shout
print(yell("hi"))

'''
here we have assigned the function shout to a variable.
This will not call the function instead it takes the function object
refrenced by shout and creates a second name pointing to it.
'''
#----------------------------------------------------
