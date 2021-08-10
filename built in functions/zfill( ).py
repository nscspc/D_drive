t="program is fun"
print(t.zfill(15))
print(t.zfill(20))
print(t.zfill(10))

#working of zfill( ) with sign(+,-) prefix :
n="-45"
print(n.zfill(8))

n="+45"
print(n.zfill(8))

t="--random+text"
print(t.zfill(20))

'''
The zfill() method returns a copy of the string with '0' characters padded to the left.

The syntax of zfill() in Python is:

str.zfill(width)
zfill() Parameter
zfill() takes a single character width.

The width specifies the length of the returned string from zfill() with 0 digits filled to the left.

Return Value from zfill()
zfill() returns a copy of the string with 0 filled to the left. The length of the returned string depends on the width provided.

Suppose, the initial length of the string is 10. And, the width is specified 15. In this case, zfill() returns a copy of the string with five '0' digits filled to the left.
Suppose, the initial length of the string is 10. And, the width is specified 8. In this case, zfill() doesn't fill '0' digits to the left and returns a copy of the original string. The length of the returned string in this case will be 10.

'''
