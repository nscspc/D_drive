Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x=[4,5,6]
>>> 
>>> x.remove(5)
>>> x
[4, 6]
>>> del x[1]
>>> x
[4]
>>> y=[1,2,3,4,2,4]
>>> y.remove(2)
>>> y
[1, 3, 4, 2, 4]
>>> y.remove(3)
>>> y
[1, 4, 2, 4]
>>> 


Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x=[1.1.1.1.1.1.,1,1,1,2]
SyntaxError: invalid syntax
>>> x=[1.1.1.1.1.1,1,1,1,2]
SyntaxError: invalid syntax
>>> x=[1.1,1,1,1,2]
>>> x.remove()
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    x.remove()
TypeError: remove() takes exactly one argument (0 given)
>>> x.remove(0)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    x.remove(0)
ValueError: list.remove(x): x not in list
>>> x.remove(1)
>>> x
[1.1, 1, 1, 2]
>>> x=[1,2,1,2]
>>> x.remove(1)
>>> x
[2, 1, 2]
>>> x.remove()
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    x.remove()
TypeError: remove() takes exactly one argument (0 given)
>>> x.remove( )
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    x.remove( )
TypeError: remove() takes exactly one argument (0 given)
>>> 
