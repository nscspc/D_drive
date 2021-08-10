Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.


>>> t1=(1,2,3)


>>> t2=(4,5,6)


>>> t1+t2
(1, 2, 3, 4, 5, 6)


>>> t3=(7,8,9)


>>> t1+t2+t3
(1, 2, 3, 4, 5, 6, 7, 8, 9)


>>> t1+2
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    t1+2
TypeError: can only concatenate tuple (not "int") to tuple


>>> t2+'abc'
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    t2+'abc'
TypeError: can only concatenate tuple (not "str") to tuple


>>> t3+(3)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    t3+(3)
TypeError: can only concatenate tuple (not "int") to tuple


>>> t3+(3,)
(7, 8, 9, 3)


>>> t3
(7, 8, 9)


>>> t3+(3,4)
(7, 8, 9, 3, 4)


>>> t3
(7, 8, 9)


>>> 
