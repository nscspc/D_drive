Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> employees={'name': 'john', 'age': 24, 'salary': 10000}
>>> employees.remove()
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    employees.remove()
AttributeError: 'dict' object has no attribute 'remove'
>>> employees.clear()
>>> employees
{}
>>> 