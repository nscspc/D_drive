Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.


>>> t1=(5,7,3,9,12)


>>> del t1[1]
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    del t1[1]
TypeError: 'tuple' object doesn't support item deletion


>>> del t1


>>> t1
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    t1
NameError: name 't1' is not defined


>>> print(t1)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    print(t1)
NameError: name 't1' is not defined


>>> 
