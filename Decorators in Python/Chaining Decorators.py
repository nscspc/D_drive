# Chaining Decorators :-
'''
Chaining Decorators simply means decorating a function with multiple
decorators.
'''
def decor1(func):
    def inner():
        x=func()
        return x*x
    return inner

def decor(func):
    def inner():
        x=func()
        return x*2
    return inner

@decor1
@decor
def num():
    return 10

print(num())

'''
The above example is similar to calling the function as –

decor1(decor(num))
'''
