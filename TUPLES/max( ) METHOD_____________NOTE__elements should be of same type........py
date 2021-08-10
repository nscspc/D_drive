Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.


>>> t=(10,12,14,20,22,24,30,32,34)


>>> max(t)
34


>>> t1=('karan','zubin','zara','ana')


>>> max(t1)
'zubin'


>>> ab=(1,2.5,"1',[3,4],(3,4))
	
SyntaxError: EOL while scanning string literal


>>> ab=(1,2.5,"1",[3,4],(3,4))
	
>>> max(ab)
	
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    max(ab)
TypeError: '>' not supported between instances of 'str' and 'float'


>>> ab=(1,2.5,"1",[3,4])
	
>>> max(ab)
	
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    max(ab)
TypeError: '>' not supported between instances of 'str' and 'float'


>>> ab=([3,4],(3,4))
	
>>> max(ab)
	
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    max(ab)
TypeError: '>' not supported between instances of 'tuple' and 'list'


>>> 
