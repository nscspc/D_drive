# Arbitrary Arguments :- *args
'''
if you we do not know how many arguments that
will be passed into the function , so add a * before
the parameter name in the function defination .

'''
'''This way the function will receive a tuple of arguments,
and can access the items accordingly :-'''

def mf(*kids):
    print("the youngest child is "+kids[2])

mf("a","b","C")
