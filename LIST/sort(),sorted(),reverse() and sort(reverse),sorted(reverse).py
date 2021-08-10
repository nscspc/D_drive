Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x=[1,02,0,4,0,5,85,0,4]
SyntaxError: invalid token
>>> x=[1,0.2,0,4,0,5,85,0,4]
>>> x
[1, 0.2, 0, 4, 0, 5, 85, 0, 4]
>>> x.reverse()
>>> x
[4, 0, 85, 5, 0, 4, 0, 0.2, 1]
>>> x.reverse(sort())
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    x.reverse(sort())
NameError: name 'sort' is not defined
>>> x.reverse(x.sort())
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    x.reverse(x.sort())
TypeError: reverse() takes no arguments (1 given)
>>> x.reverse(x.sorted())
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    x.reverse(x.sorted())
AttributeError: 'list' object has no attribute 'sorted'
>>> x.reverse(sorted(x))
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    x.reverse(sorted(x))
TypeError: reverse() takes no arguments (1 given)
>>> sorted(x,reverse="true"))
SyntaxError: invalid syntax
>>> sysclear()
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    sysclear()
NameError: name 'sysclear' is not defined
>>> sys.clear()
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    sys.clear()
NameError: name 'sys' is not defined
>>> import system
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    import system
ModuleNotFoundError: No module named 'system'
>>> x=[1,0,2,4,5,1]
>>> sorted(x)
[0, 1, 1, 2, 4, 5]
>>> print(sorted(x))
[0, 1, 1, 2, 4, 5]
>>> x
[1, 0, 2, 4, 5, 1]
>>> print(x.sort())
None
>>> x.sort(0:2)
SyntaxError: invalid syntax
>>> x.sort([0:2])
SyntaxError: invalid syntax
>>> x[0:3].sort()
>>> x
[0, 1, 1, 2, 4, 5]
>>> x.append(0)
>>> x
[0, 1, 1, 2, 4, 5, 0]
>>> x[0:3].sort()
>>> x
[0, 1, 1, 2, 4, 5, 0]
x
>>> 
>>> x[3:len(x)-1].sort()
>>> x
[0, 1, 1, 2, 4, 5, 0]
>>> x[3:len(x)].sort()
>>> x
[0, 1, 1, 2, 4, 5, 0]
>>> x[3:len(x)+1].sort()
>>> x
[0, 1, 1, 2, 4, 5, 0]
>>> x.insert(,99)
SyntaxError: invalid syntax
>>> x.insert(0,99)
>>> x
[99, 0, 1, 1, 2, 4, 5, 0]
>>> x[0:3].sort()
>>> x
[99, 0, 1, 1, 2, 4, 5, 0]
>>> x.sort()
>>> x
[0, 0, 1, 1, 2, 4, 5, 99]
>>> x.sort(reverse=True)
>>> x
[99, 5, 4, 2, 1, 1, 0, 0]
>>> sorted(x,reverse=True)
[99, 5, 4, 2, 1, 1, 0, 0]
>>> y=[1,0,7,2,4,0]
>>> sorted(y,reverse=)
SyntaxError: invalid syntax
>>> sorted(y,reverse=True)
[7, 4, 2, 1, 0, 0]
>>> x
[99, 5, 4, 2, 1, 1, 0, 0]
>>> y
[1, 0, 7, 2, 4, 0]
>>> y.reverse(sort=True)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    y.reverse(sort=True)
TypeError: reverse() takes no keyword arguments
>>> y.reverse(sorted()=True)
SyntaxError: keyword can't be an expression
>>> y.reverse(y.sorted()=True)
SyntaxError: keyword can't be an expression
>>> 
