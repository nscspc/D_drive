#execution time of a function
import time
import math

def calculate_time(func):
    def inner1(*args,**kwargs):#*args for many no. of arguments if we don't know the no. of arguments # and *kwargs for the keyword arguments means the arguments defined using some keywords while calling the function.
        begin=time.time()
        func(*args,**kwargs)
        end=time.time()
        print("Total time taken by : ",func.__name__,"=",end-begin)
    return inner1

@calculate_time
def factorial(num):
    time.sleep(2)
    print(math.factorial(num))

factorial(10)
