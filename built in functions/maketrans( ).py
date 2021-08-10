# .maketrans( ): prints the ascii value of the key(which should be a character , not a string , and not a number) means there can only be 1 letter as the key in the dictionary and argument of this function can only be a dictionary #

#translation table using a dictionary with maketrans( )
string=""
dict={"a":123,"s":'af'}
print(string.maketrans(dict))

dict={45:123,86:'af'}
string=""
print(string.maketrans(dict))

#translation table using 2 strings with maketrans( )
fs="abc"
ss="deg"
string=""#string can be any string like : string="abc"
print(string.maketrans(fs,ss))

#translation table with removable string with maketrans( )
fs="abc"
ss="def"
ts="abd"
s=""
print(s.maketrans(fs,ss,ts))

'''
Here, first, the mapping between the two strings firstString and secondString are created.

Then, the third argument thirdString resets the mapping of each character in it to None and also creates a new mapping for non-existent characters.

In this case, thirdString resets the mapping of 97 ('a') and 98 ('b') to None, and also creates a new mapping for 100 ('d') mapped to None.

'''
sd="xsdada"
print(string.maketrans(fs,sd))#error  : as these 2 arguments must have same length
