Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.


>>> sqrs=(0,1,4,9,16,25,36,49,64,81,100,121,144,169,196,225,256,289,324,361,400,441,484,529,576,625)


>>> sqrs(10)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    sqrs(10)
TypeError: 'tuple' object is not callable


>>> sqrs[10]
100


>>> sqrs[10:20]
(100, 121, 144, 169, 196, 225, 256, 289, 324, 361)


>>> sqrs[10:-10]
(100, 121, 144, 169, 196, 225)


>>> sqrs[10:20:25]
(100,)


>>> sqrs[20:22:25]
(400,)
>>> 
