#when we create a tuple , we normally assign values to it , this is called "packing" a tuple .
fruits=("apple","banana","cherry")

# to extract values back into variables , this is called "unpacking" .
(green,yellow,red)=fruits
print(green)
print(yellow)
print(red)
print()
# using asterisk (*)

(green,yellow,*red)=fruits
print(green)
print(yellow)
print(red)
print()
fruits=("apple","banana","cherry","strawberry","raspberry")
(green,yellow,*red)=fruits
print(green)
print(yellow)
print(red)
print()

#unpacking using a list of variables instead of tuple of variables
fruits=("apple","banana","cherry","strawberry","raspberry")
[green,yellow,*red]=fruits
print(green)
print(yellow)
print(red)
print()

#unpacking a list using tuple of variables
fruits=["apple","banana","cherry","strawberry","raspberry"]
(green,yellow,*red)=fruits
print(green)
print(yellow)
print(red)
print()

#unpacking a list using a list of variables
fruits=["apple","banana","cherry","strawberry","raspberry"]
[green,yellow,*red]=fruits
print(green)
print(yellow)
print(red)
print()

# changing the asterisk( * ) variable :-
fruits=["apple","banana","cherry","strawberry","raspberry"]
[green,*yellow,red]=fruits
print(green)
print(yellow)
print(red)
print()

fruits=["apple","banana","cherry","strawberry","raspberry","a","b"]
[green,*yellow,red]=fruits
print(green)
print(yellow)
print(red)
print()
# it means that in this case it leaves the last value for last variable and remaining values in the asterisk variable
