# to remove a value from a set #
num_set={1,2,3,4,5,6}
num_set.discard(3)
print(num_set)

num_set.remove(5)
print(num_set)

num_set.discard(5)#no error occured even the value is already not present in the set
print(num_set)

#but the error occurs when the same thing is done with remove( ) :-
try:
    num_set.remove(5)
    print(num_set)
except:
    print("error occured")

'''
With the pop() method, we can remove and return an element.
Since the elements are unordered,
we cannot tell or predict the item that will be removed.
'''
num_set.pop()
print(num_set)

num_set.pop()
print(num_set)

num_set.pop()# error : in this case pop( ) function does not takes any argument #
print(num_set)

# clear( ) function removes all the elements in the set and empty set is obtained
num_set.clear( )
print(num_set)

#The del keyword will delete the set completely:
del num_set
print(num_set)
