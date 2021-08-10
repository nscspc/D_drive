Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x=[4,5,6,9]
>>> x.index(2)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    x.index(2)
ValueError: 2 is not in list
>>> x.index(4)
0
>>> 
>>> 2
2
>>> 
>>> x.index[4]
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    x.index[4]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> 

>>> x.index(5)
4
>>> x.index(1)
0
>>> x.index(6)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    x.index(6)
ValueError: 6 is not in list
>>>

#index function is used to find the index of a particular element in the list#
