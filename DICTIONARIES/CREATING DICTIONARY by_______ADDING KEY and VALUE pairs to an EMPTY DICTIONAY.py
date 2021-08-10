Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> employees={}
>>> employee['name']='john'
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    employee['name']='john'
NameError: name 'employee' is not defined
>>> employees['name']='john'
>>> employees['age']=24
>>> employees['salary']=10000
>>> employees
{'name': 'john', 'age': 24, 'salary': 10000}
>>> students=dict()
>>> students
{}
>>> students['name']='naveen'
>>> students['name']='manish'
>>> students['name']
'manish'
>>> 
