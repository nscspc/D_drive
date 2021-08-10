Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> employees={'name': 'john', 'age': 24, 'salary': 10000}

>>> employees.items()
dict_items([('name', 'john'), ('age', 24), ('salary', 10000)])
>>> myLIST=employees.items()
>>> for x in myLIST:
	print(x)

	
('name', 'john')
('age', 24)
('salary', 10000)
>>> seq=employees.items()
>>> for key,val in seq:
	print(key,val)

	
name john
age 24
salary 10000
>>> for ky,vl in seq:
	print(key,val)

	
salary 10000
salary 10000
salary 10000
>>> seq=employees.items()
>>> for ky,vl in seq:
	print(key,val)

	
salary 10000
salary 10000
salary 10000
>>> seq=employees.items()
>>> for ky,vl in seq:
	print(key, val)

	
salary 10000
salary 10000
salary 10000
>>> 
