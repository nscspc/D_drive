# setdefault( ) :- this method returns the value of the item with the specified key .
#                    , if the 'key does not exist' , 'insert the key' , 'with  the specified value' .
#syntax :-
#           dict_name.setdefault(keyname,value)

'''
Parameter Values

Parameter	Description
keyname	         Required. The keyname of the item you want to return the value from
value	         Optional.
                     If the key exist, this parameter has no effect.
                     If the key does not exist, this value becomes the key's value
                     Default value None

'''

d={
    1:2,
    2:3,
    3:4,
    4:5
    }
x=d.setdefault(4,10)
print(x)
print(d)
print()

y=d.setdefault(10)
print(y)
print(d)
print()

y=d.setdefault(10,20)
print(y)
print(d)
print()
#means if a value is set default then it does not change , even after initializing it again .

z=d.setdefault(20,20)
print(z)
print(d)
print()

z=d.setdefault(30)
print(z)
print(d)
print()
