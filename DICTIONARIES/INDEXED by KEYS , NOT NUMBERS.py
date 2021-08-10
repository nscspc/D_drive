Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> dict1={0:'value for key 0',1:'value for key one','3':'value for a string as a key',(4,5):'value for a tuple as a key','and for fun':7}
>>> dict1[0]
'value for key 0'
>>> dict1[(4,5)]
'value for a tuple as a key'
>>> dict1[4,5]
'value for a tuple as a key'
>>> dict1(4,5)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    dict1(4,5)
TypeError: 'dict' object is not callable
>>> dict1['3']
'value for a string as a key'
>>> dict1['and for fun']
7
>>> dict1[7]
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    dict1[7]
KeyError: 7
>>> 
