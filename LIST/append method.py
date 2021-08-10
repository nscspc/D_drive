Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x=[4,5,6]
>>> x.append(5)
>>> print x
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(x)?
>>> printx
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    printx
NameError: name 'printx' is not defined
>>> x
[4, 5, 6, 5]
>>> x.append[5]
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    x.append[5]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> 
