Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.


>>> t=tuple()
>>> t
()


>>> t=tuple([1,2,3])
>>> t
(1, 2, 3)


>>> t=tuple('abc')
>>> t
('a', 'b', 'c')


>>> t1=tuple({1:'1',2:'2'})
>>> t1
(1, 2)
>>> t1
(1, 2)


>>> t2=tuple(1)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    t2=tuple(1)
TypeError: 'int' object is not iterable


>>> 
