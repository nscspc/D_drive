Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> employees=dict({'name'='john','age'=24,'salary'=10000})
SyntaxError: invalid syntax
>>> employees=dict({name='john',age=24,salary=10000})
SyntaxError: invalid syntax
>>> employees=dict({name='john',age=24,salary=10000})
SyntaxError: invalid syntax
>>> employees=dict({name:'john',age:24,salary:10000})
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    employees=dict({name:'john',age:24,salary:10000})
NameError: name 'name' is not defined
>>> employees=dict({'name':'john','age':24,'salary':10000})
>>> employees
{'name': 'john', 'age': 24, 'salary': 10000}
>>> 
