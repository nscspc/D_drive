Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> BMI=W**2/H
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    BMI=W**2/H
NameError: name 'W' is not defined
>>> BMI=w**2/h
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    BMI=w**2/h
NameError: name 'w' is not defined
>>> bmi=w**2/h
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    bmi=w**2/h
NameError: name 'w' is not defined
>>> W=45kg
SyntaxError: invalid syntax
>>> w=45kg
SyntaxError: invalid syntax
>>> w=float(input("n"))
n45kg
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    w=float(input("n"))
ValueError: could not convert string to float: '45kg'
>>> w=float(input("n"))
n45
>>> h=float(input("n"))
n5.5
>>> B M I=w**2/h
SyntaxError: invalid syntax
>>> BMI=w**2/h
>>> print(bmi)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    print(bmi)
NameError: name 'bmi' is not defined
>>> print(BMI)
368.1818181818182
>>> w=float(input("n"))
n45
>>> h=float(input("n"))
n165#height should be in cm
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    h=float(input("n"))
ValueError: could not convert string to float: '165#height should be in cm'
>>> w=float(input("n"))#kg
n45
>>> h=float(input("n"))#cm
n165
>>> BMI=w**2/h
>>> print(BMI)
12.272727272727273
>>> bmi=w/h**2




