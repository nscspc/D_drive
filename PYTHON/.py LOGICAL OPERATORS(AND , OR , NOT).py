Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x=10
>>> y=20
>>> z=41
>>> if x>y and x>z:
	print("x is greater")
elif y>x andy>z:
	
SyntaxError: invalid syntax
>>> if x>y and x>z:
	print("x is greater")
elif y>x and y>z:
	print("y is greater")
else:
	print("z is greater")

	
z is greater
>>> if a>b and a>c anda>d:
	
SyntaxError: invalid syntax
>>> if a>b and a>c and a>d:
	print("a is greater")
elif b>a and b>c and b>d:
	print("b is greater")
elif c>a and c>b and c>d:
	print("c is greater")
else:
	print("d is greater")

	
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    if a>b and a>c and a>d:
NameError: name 'a' is not defined
>>> a=1.8
>>> b=1.4
>>> c=2.0
>>> d=4
>>> if a>b and a>c and a>d:
	print("a is greater")
elif b>a and b>c and b>d:
	print("b is greater")
elif c>a and c>b and c>d:
	print("c is greater")
else:
	print("d is greater")

	
d is greater
>>> if a>b and a>c and a>d:
	print("a is greater")
elif b>a and b>c and b>d:
	print("b is greater")
elif c>a and c>b and c>d:
	print("c is greater")
elif d>a and d>b and d>c:
	print("d is greater")

	
d is greater
>>> 
