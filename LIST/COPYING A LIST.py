Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x=[1,2,3,4]
>>> y=x
>>> y
[1, 2, 3, 4]
>>> print y
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(y)?
>>> printy
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    printy
NameError: name 'printy' is not defined
>>> 
