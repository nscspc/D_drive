#to create a empty set:-
'''
The creation of an empty set is some-what tricky. If you use empty curly braces {} in Python,
you create an empty dictionary rather than an empty set. For example:
'''
s={}
print(type(s))

s=set()
print(type(s))
