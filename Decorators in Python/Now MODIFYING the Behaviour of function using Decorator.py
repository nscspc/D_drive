# Decorators
'''
As stated above the decorators are used to modify the behavior
of function or class. In Decorators, functions are taken as the
argument into another function and then called inside the wrapper
function.
'''

# Syntax for Decorator:-
'''
@gfg_decorator
def hello_decorator():
    print("Gfg")

# Above code is equivalent to :-

def hello_decorator():
    print("Gfg")

hello_decorator=gfg_decorator(hello_decorator)

'''
'''
in above code , gfg_decorator is a callable function , it will add some
code on the top of some another callable function ( hello_decorator
function ) and return the wrapper function.
'''
# Decorator can modify the behaviour of a function :-

    #defining a decorator
def hello_decorator(func):
    # inner1( ) is a wrapper function , in which the argument is called , and inner1( ) function can access the outer local function like in this case "func".
    def inner1():
        print("Hello , this is before function execution")
        #now calling the actual funtion inside the wrapper function:-
        func()
        print("This is after function execution")
    return inner1

    #defining a function to be called inside the wrapper function
def function_to_be_used():
    print("This is inside the function ! !")

    #now passing 'function_to_be_used' inside the decorator to control its behaviour :-
function_to_be_used=hello_decorator(function_to_be_used)
function_to_be_used()
