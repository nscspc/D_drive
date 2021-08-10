Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def display(x,y):
	return x+y

>>> desplay(10)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    desplay(10)
NameError: name 'desplay' is not defined
>>> display(10)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    display(10)
TypeError: display() missing 1 required positional argument: 'y'
>>> def display(x,y=2):
	return x+y

>>> display(10)
12
>>> display(10,4)
14
>>> s
