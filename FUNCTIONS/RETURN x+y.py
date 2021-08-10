Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def display(x,y):
	sum=x+y
	print(sum)

	
>>> display(5,6)
11
>>> r=display(5,6)
11
>>> r
>>> print(r)
None
>>> print(display(5,6))
11
None
>>> def display(x,y):
	return x+y

>>> display(5,6)
11
>>> r=display(5,6)
>>> r
11
>>> print(r)
11
>>> print(display(5,6))
11
>>> 
