Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x=[4,5,6]
>>> x.clear(4)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    x.clear(4)
TypeError: clear() takes no arguments (1 given)
>>> x.clear(1)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    x.clear(1)
TypeError: clear() takes no arguments (1 given)
>>> x.clear[1]
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    x.clear[1]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> x.clear()
>>> x
[]
>>> 
