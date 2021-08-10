# dict_name.pop(key) : to pop (or delete) the item (key and value) .

d={1:2,2:3,3:4,4:5}
print(d)
print()
d.pop(2)
print(d)
print()

#d.pop()# error as no argument is given
# for this popitem() function is there
#print(d)
#print()

# dict_name.popitem( ) :- this removes the last inserted item from the dictionary .
d.popitem( )
print(d)
print()

# del dict_name[key] :- del method to remove a particular key-value pair .
del d[1]
print(d)
print()

# del dict_name :- to completely delete the dictionary .
del d
#print(d)
print()

# dict_name.clear() : empties the dictionary .,it does not deletes the dictionary completely.
d={1:2,2:3,3:4,4:5}
d.clear()
print(d)


