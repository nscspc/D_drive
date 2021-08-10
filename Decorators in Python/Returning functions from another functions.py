# Returning function from another function :-

def create_adder(x):
    def adder(y):
        return x+y
    return adder

add_15=create_adder(15)
print(add_15(10))

'''
In the above example, we have created a function inside of another
function and then have returned the function created inside.
'''
