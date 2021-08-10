x="ab\tc\td:"
print(x.expandtabs())
print(x)
print(x.expandtabs(10))
print(x.expandtabs(20))
# expandtabs( ) does not work for space , it only works for tabs #
y="ab cd"
print(y.expandtabs(10))

'''
ab      c       d:
|       |=8
ab	c	d:
ab        c         d:
ab                  c                   d:
|                   |=20 
'''
'''
Python String expandtabs()
The expandtabs() method returns a copy of string with all tab characters '\t' replaced with whitespace characters until the next multiple of tabsize parameter.

The syntax of expandtabs() method is:

string.expandtabs(tabsize)


expandtabs() Parameters
The expandtabs() takes an integer tabsize argument. The default tabsize is 8.

Return Value from expandtabs()
The expandtabs() returns a string where all '\t' characters are replaced with whitespace characters until the next multiple of tabsize parameter.

'''
