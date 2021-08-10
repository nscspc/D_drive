Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
 
>>> n1=int(input("no."))
no.1
>>> 
>>> n2=int(input("no."))
no.2
>>> n3=int(input("no."))
no.4
>>> s=n1+n2+n3
>>> print("the 3no. are" ,n1,n2,n3 "and their sum is",s)
SyntaxError: invalid syntax

>>> print("the 3no. are" ,n1,n2,n3 ,"and their sum is",s)
the 3no. are 1 2 4 and their sum is 7

>>> print("the 3 no. are" ,n1,n2,n3 ,"and their sum is",s)
the 3 no. are 1 2 4 and their sum is 7

>>> print("the 3 no. are" n1,n2,n3 "and their sum is" s)
SyntaxError: invalid syntax

>>> print("the 3 no. are",n1,n2,n3,"and their sum is",s)
the 3 no. are 1 2 4 and their sum is 7

>>> print("the 3 no. are", n1,n2,n3, "and their sum is", s)
the 3 no. are 1 2 4 and their sum is 7

>>> print("the 3 no. are", n1,n2,n3, "and their sum is", s,.)
SyntaxError: invalid syntax

>>> print("the 3 no. are", n1,n2,n3, "and their sum is", s,'.')
the 3 no. are 1 2 4 and their sum is 7 .
