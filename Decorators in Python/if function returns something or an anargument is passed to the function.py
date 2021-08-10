# if a function returns something or an argument is passed to the function :-
def hello_decorator(func):
    def inner1(*args, **kwargs):
          
        print("before Execution")
          
        # getting the returned value
        returned_value = func(*args, **kwargs)
        print("after Execution")
          
        # returning the value to the original frame
        return returned_value
          
    return inner1
  
  
# adding decorator to the function
@hello_decorator
def sum_two_numbers(a, b):
    print("Inside the function")
    return a + b
  
a, b = 1, 2
  
# getting the value through return of the function
print("Sum =", sum_two_numbers(a, b))

'''
In the above example, you may notice a keen difference in the
parameters of the inner function. The inner function takes the
argument as *args and **kwargs which means that a tuple of
positional arguments or a dictionary of keyword arguments can
be passed of any length. This makes it a general decorator that
can decorate a function having any number of arguments.

'''
