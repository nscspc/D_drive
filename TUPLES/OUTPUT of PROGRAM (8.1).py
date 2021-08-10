Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> t=('hello','isn't','python','fun','?')
       
SyntaxError: invalid syntax
>>> t=('hello','isn`t','python','fun','?')
       
>>> length=len(t)
       
>>> for a in range(length):
       print('at indexes',a,'and',(a-length),'element :',t[a])

       
at indexes 0 and -5 element : hello
at indexes 1 and -4 element : isn`t
at indexes 2 and -3 element : python
at indexes 3 and -2 element : fun
at indexes 4 and -1 element : ?
>>> 
========== RESTART: C:/Users/Home/Desktop/PROGRAM of TUPLE (8.1).py ==========
at indexes 0 and -5 element : hello
at indexes 1 and -4 element : isn`t
at indexes 2 and -3 element : python
at indexes 3 and -2 element : fun
at indexes 4 and -1 element : ?
>>> 
