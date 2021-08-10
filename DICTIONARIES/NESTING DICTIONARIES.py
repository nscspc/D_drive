Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.


>>> employees={'john':{'age': 25, 'salary': 20000},'diya':{'age':35,'salary'=500000}}
SyntaxError: invalid syntax


>>> employees={'john':{'age': 25, 'salary': 20000},'diya':{'age':35,'salary':50000}}


>>> employees
{'john': {'age': 25, 'salary': 20000}, 'diya': {'age': 35, 'salary': 50000}}


>>> print('employees',key,':')
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    print('employees',key,':')
NameError: name 'key' is not defined


>>> for key in employees:
	print('employees',key,':')
	print('age:',str(employees[key]['age']))
	print('salary:',str(employees[key]['salary']))

	
employees john :
age: 25
salary: 20000
employees diya :
age: 35
salary: 50000


>>> for key in employees:
	print('employees',key,':')
	print('age:',(employees[key]['age']))
	print('salary:',(employees[key]['salary']))

	
employees john :
age: 25
salary: 20000
employees diya :
age: 35
salary: 50000


>>> for key in employees:
	print('employees',key,':')
	print('age:',string(employees[key]['age']))
	print('salary:',string(employees[key]['salary']))

	
employees john :
Traceback (most recent call last):
  File "<pyshell#12>", line 3, in <module>
    print('age:',string(employees[key]['age']))
NameError: name 'string' is not defined


>>> employees['john']
{'age': 25, 'salary': 20000}


>>> employees['john'['age']]
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    employees['john'['age']]
TypeError: string indices must be integers


>>> employees['john']['age']
25
>>> 
