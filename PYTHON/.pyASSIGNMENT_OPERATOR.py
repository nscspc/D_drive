Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x=x+5
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    x=x+5
NameError: name 'x' is not defined
>>> x+=5
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    x+=5
NameError: name 'x' is not defined
>>> x=1
>>> x=x+5
>>> x
6
>>> x+=6
>>> x
12
>>> y=1
>>> y=y/10
>>> y
0.1
>>> y/=10
>>> y
0.01
>>> y=1
>>> y/=10
>>> y
0.1
>>> m=7
>>> m=m-2
>>> m
5
>>> m=7
>>> m-=2
>>> m
5
>>> n=4
>>> n=n*4
>>> n
16
>>> 
>>> n=4
>>> n*=4
>>> n
16
>>> n=4
>>> n**=4
>>> n
256
>>> n=4
>>> n%=4
>>> n
0
>>> n=4
>>> n//=4
>>> n
1
>>> 
