Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.


>>> vowels={'a','e','i','o','u'}


>>> vowels[0]
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    vowels[0]
TypeError: 'set' object does not support indexing


>>> vowels
{'e', 'a', 'o', 'i', 'u'}


>>> vowels=('a','e','i','o','u')


>>> vowels[0]
'a'


>>> vowels[4]
'u'


>>> vowels[-1]
'u'


>>> vowels[-5]
'a'


>>> 
