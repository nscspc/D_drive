Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x=[4,5,6]
>>> x.nsert(2,99)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    x.nsert(2,99)
AttributeError: 'list' object has no attribute 'nsert'
>>> x.insert(2,99)
>>> x
[4, 5, 99, 6]
>>> 
