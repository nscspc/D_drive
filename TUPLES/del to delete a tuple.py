#tuple is immutable but it can be deleted
t=tuple((1,2,3,4,5))
print(t)
del t
print(t)#NameError : name 't' is not defined
