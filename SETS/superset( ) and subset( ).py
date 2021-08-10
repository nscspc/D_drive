#set comparison
'''
we can compare sets depending on the elements they have .
this way , we can tell whether a set is a 'superset'  or a 'subset'
of another set.

'''
s1={1,2,3,4,5}
s2={2,3}
print(s1<=s2)
print( )
print(s1>=s2)
print( )
print(s2<=s1)
print( )
print(s2>=s1)
print( )
print( )

# using issubset( ) and superset( ) :-
print(s1.issuperset(s2))
print( )
print(s1.issubset(s2))
print( )
