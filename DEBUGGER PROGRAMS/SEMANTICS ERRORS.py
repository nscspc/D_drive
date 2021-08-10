Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> z=x*y
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    z=x*y
NameError: name 'x' is not defined
>>> x=0
>>> y=0
>>> z=x*y
>>> x*y=z
SyntaxError: can't assign to operator
>>> 
