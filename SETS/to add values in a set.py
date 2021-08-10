#to add values in a set
s={1,'n','aasa',(),}
print(s)
s.add("sas")
print(s)
print()

#as in output the order of values changes because :-
#A set is an unordered data structure, so it does not preserve the insertion order.#

#so to access the values in initial order :-
#sorted(s, key=s.index)

l=[1,3,2,5,4]
print(set(l))
print()

'''
output:

{1, 2, 3, 4, 5}

#now the order gets changed
'''
#so to access the values in initial order :-
nls=sorted(set(l),key=l.index)
print(nls)
print()

'''
------------------------------
Introduction
How to Create a Set
Accessing Set Items
Adding Items to a Set
Removing Items from a Set
Set Union
Set Intersection
Set Difference
Set Comparison
Set Methods
Python Frozen Set
Conclusion
------------------------------

Introduction

In Python, a set is a data structure that stores unordered items. The set items are also unindexed. Like a list, a set allows the addition and removal of elements. However, there are a few unique characteristics that define a set and separate it from other data structures:

A set does not hold duplicate items.
The elements of the set are immutable, that is, they cannot be changed, but the set itself is mutable, that is, it can be changed.
Since set items are not indexed, sets don't support any slicing or indexing operations.

