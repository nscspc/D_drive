Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> t=('p','y','t','h','o','n')
>>> for a in t:
	print(a)

	
p
y
t
h
o
n
>>> for a in t:
	print(t[a])

	
Traceback (most recent call last):
  File "<pyshell#5>", line 2, in <module>
    print(t[a])
TypeError: tuple indices must be integers or slices, not str
>>> t=('p','y','t','h','o','n')
>>> for a in t:
	print(t[a])

	
Traceback (most recent call last):
  File "<pyshell#8>", line 2, in <module>
    print(t[a])
TypeError: tuple indices must be integers or slices, not str
>>> 
