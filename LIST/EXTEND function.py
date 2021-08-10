Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x=[4,5,6]
>>> x.extend(10)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    x.extend(10)
TypeError: 'int' object is not iterable
>>> x.extend(10,5)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    x.extend(10,5)
TypeError: extend() takes exactly one argument (2 given)
>>> x.extend[10,5]
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    x.extend[10,5]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> x
[4, 5, 6]
>>> x.extend [10,5]
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    x.extend [10,5]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> x extend [10,5]
SyntaxError: invalid syntax
>>> x extend(10,5)
SyntaxError: invalid syntax
>>> x.extnd(10,5)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    x.extnd(10,5)
AttributeError: 'list' object has no attribute 'extnd'
>>> 
