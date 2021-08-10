Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x=1
>>> y=2
>>> x=y
>>> x
2
>>> y=x+2
>>> y
4
>>> x
2
>>> x=y
>>> y=x+2
>>> x
4
>>> y
6
>>> x=y
>>> y=x+2
>>> y
8
>>> x
6
>>> x,y=1,2
>>> x,y=y,x+2

>>> print(x,y)
2 3
>>> print(x,y)
2 3
>>> (x,y)
(2, 3)
>>> print(x,y)
2 3
>>> ]x,y[
	
SyntaxError: invalid syntax
>>> [x,y]
[2, 3]
>>> x,y=7,2
>>> x,y,x=x+1,y+3,x+10
>>> print(x,y)
17 5
>>> 
