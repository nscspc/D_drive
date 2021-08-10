Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x=input("enter no.")#10
enter no.10
>>> kjlhiglii
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    kjlhiglii
NameError: name 'kjlhiglii' is not defined
>>> x=input("enter no.")
enter no.10
>>> y=input("enter no.")
enter no.10
>>> sum=x+y
>>> sum
'1010'
>>> x=input("enter no.")#10
enter no.
>>> y=input("enter no.")#20
enter no.
>>> sum=x+y
>>> sum
''
>>> x=int(input("enter no."))
enter no.44
>>> y=float(input("enter no."))
enter no.88
>>> sum=x+y
>>> sum
132.0
>>> y=int(input("enter no."))
enter no.88
>>> sum
132.0
>>> x=int(input("enter no."))
enter no.44
>>> y=int(input("enter no."))
enter no.88
>>> sum=x+y
>>> sum
132
>>> x=float(input("enter no."))
enter no.44
>>> y=float(input("enter no."))
enter no.88
>>> sum=x+y
>>> sum
132.0
>>> x=float(input("enter no."))#10
enter no.
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    x=float(input("enter no."))#10
ValueError: could not convert string to float: 
>>> x=float(input("enter no.")) #10
enter no.
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    x=float(input("enter no.")) #10
ValueError: could not convert string to float: 
>>> x=(input("enter no.")) #10
enter no.
>>> y=(input("enter no.")) #10
enter no.
>>> x+y
''
>>> x=input("enter no.") #10
enter no.
>>> y=input("enter no.") #10
enter no.
>>> z=x+y
>>> z
''
>>> 
