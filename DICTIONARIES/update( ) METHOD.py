Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> employees={'name': 'john', 'age': 24, 'salary': 10000}


>>> employee=employees={'name': 'diya', 'age': 34, 'salary': 20000,'dept'='sales'}
SyntaxError: invalid syntax


>>> employee=employees={'name': 'diya', 'age': 34, 'salary': 20000,'dept':'sales'}


>>> employees.update(employee)


>>> employees
{'name': 'diya', 'age': 34, 'salary': 20000, 'dept': 'sales'}


>>> employees={'name': 'john', 'age': 24, 'salary': 10000}


>>> employee.update(employees)


>>> employee
{'name': 'john', 'age': 24, 'salary': 10000, 'dept': 'sales'}


>>> 
