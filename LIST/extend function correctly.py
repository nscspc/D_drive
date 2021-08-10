Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x=list(range(0,10))
>>> x
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> x.extend(14)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    x.extend(14)
TypeError: 'int' object is not iterable
>>> x.extend(str(14))
>>> x
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, '1', '4']
>>> x.extend(str("14"))
>>> x
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, '1', '4', '1', '4']
>>> x.extend([14])
>>> 
>>> x
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, '1', '4', '1', '4', 14]
>>> x.extend[14]
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    x.extend[14]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> y=list(range(1,101)
       )
>>> y
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
>>> print(y=list(range(1,101)))
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    print(y=list(range(1,101)))
TypeError: 'y' is an invalid keyword argument for print()
>>> print(list(range(1,101)))
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
>>>

>>> x=list(range(1,6))
>>> x
[1, 2, 3, 4, 5]
>>> x.extend([1,2,3,4,5])
>>> x
[1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
>>> #extend function is used to add more than 1 value in the list.#
