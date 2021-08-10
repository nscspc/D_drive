Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy
>>> ar=numpy.array([1,2])
>>> print(ar)
[1 2]
>>> type(ar)
<class 'numpy.ndarray'>
>>> ar.ndim
1
>>> ar=numpy.array([1,2],[1,2])
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    ar=numpy.array([1,2],[1,2])
TypeError: data type not understood
>>> ar=numpy.array([1,2],[1,2]);
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    ar=numpy.array([1,2],[1,2]);
TypeError: data type not understood
>>> ar=numpy.array(([1,2],[1,2]));
>>> ar
array([[1, 2],
       [1, 2]])
>>> type(ar)
<class 'numpy.ndarray'>
>>> ar.ndim
2
>>> 
