Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x=[4,5,6]
>>> del.x[1]
SyntaxError: invalid syntax
>>> del x[1]
>>> del.x[1]
SyntaxError: invalid syntax
>>> x
[4, 6]
>>> del x[0:1]
>>> x
[6]
>>> x=[4,5,6,9,4,9,6]
>>> del x[1:3]
>>> x
[4, 9, 4, 9, 6]
>>> del x [1:3]
>>> x
[4, 9, 6]
>>> del x
>>> x
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    x
NameError: name 'x' is not defined
>>> 
