Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 10/0
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    10/0
ZeroDivisionError: division by zero
>>> try:
	print("result of 10/5 =",(10/5))
	print("result of 10/0 =",(10/0))
except:
	("divide by zero! denominator must not be zero")

	
result of 10/5 = 2.0
'divide by zero! denominator must not be zero'
>>> try:
	print("result of 10/5 =",(10/5))
	print("result of 10/0 =",(10/0))
except:
	("divide by five! denominator must not be five")

	
result of 10/5 = 2.0
'divide by five! denominator must not be five'

>>> print("result of 10/5 =",(10/5))
    print("result of 10/0 =",(10/0))

	
SyntaxError: multiple statements found while compiling a single statement
>>> 
