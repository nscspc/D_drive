Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def display(x,y):
	return x+y,x-y

>>> print(display(5,6))
(11, -1)
>>> add,sum=disply(10,2)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    add,sum=disply(10,2)
NameError: name 'disply' is not defined
>>> add,sub=display(10,2)
>>> print('add =,add)
	  
SyntaxError: EOL while scanning string literal
>>> print('add ='add)
	  
SyntaxError: invalid syntax
>>> print('add =',add)
	  
add = 12
>>> print('sub =',sub)
	  
sub = 8
>>> 
