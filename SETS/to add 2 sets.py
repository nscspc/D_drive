# set1.union(set2) :- to add 2 sets
s1={1,2,True,'a'}
s2={',2,',False,True}
st=s1.union(s2)#True doesn't get added in final set
print(st)
st=s2.union(s1)
print(st)

#to add more than 2 sets :-
s3={'t','h','r','i','d'}
print(s3.union(s1,s2))

# The | operator can also be used to find the union of two or more sets. 
print(s3|s2|s1)

#The update() method inserts the items in set2 into set1:
s1.update(s2)
print(s1)

print

print(s1)
print(s2)
print(s3)
