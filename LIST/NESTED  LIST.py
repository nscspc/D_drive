Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> L=[4,5,[6,9],10]
>>> L
[4, 5, [6, 9], 10]
>>> print (L[2])
[6, 9]
>>> print (L[2,0])
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    print (L[2,0])
TypeError: list indices must be integers or slices, not tuple
>>> print (L[2,2])
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    print (L[2,2])
TypeError: list indices must be integers or slices, not tuple
>>> print (L[2,1])
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print (L[2,1])
TypeError: list indices must be integers or slices, not tuple
>>> print (L[2,3])
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    print (L[2,3])
TypeError: list indices must be integers or slices, not tuple
>>> print (L[2,4])
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    print (L[2,4])
TypeError: list indices must be integers or slices, not tuple
>>>



>>> x=[1,0,[2,4],10,'adda']
>>> x[2]
[2, 4]
>>> x[2[0]]
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    x[2[0]]
TypeError: 'int' object is not subscriptable
>>> x[[2][0]]
[2, 4]
>>> x[[2][1]]
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    x[[2][1]]
IndexError: list index out of range
>>> x[2][1]
4
>>> x[2][0]
2
>>> # syntax to access particular element from a nested list #
