Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def display()
SyntaxError: invalid syntax
>>> def display():
	print("hello")

	
>>> display()
hello
>>> display(10)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    display(10)
TypeError: display() takes 0 positional arguments but 1 was given
>>> def display:
	print("hello")
	
SyntaxError: invalid syntax
>>> 
