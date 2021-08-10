Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.


>>> employees={'name': 'john', 'age': 24, 'salary': 10000}


>>> del employee['age']
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    del employee['age']
NameError: name 'employee' is not defined


>>> del employees['salary']


>>> employees
{'name': 'john', 'age': 24}


>>> del employees['salary']
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    del employees['salary']
KeyError: 'salary'
>>> 
