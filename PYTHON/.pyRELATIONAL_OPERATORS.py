Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> 110>5
True




>>> print(110>5)
True




>>> print("110">"5")
False




>>> n>n
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    n>n
NameError: name 'n' is not defined




>>> n>l
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    n>l
NameError: name 'n' is not defined




>>> print("n">"h")
True




>>> print("h">"n")
False




>>> print("5">="5")
True




>>> print("5">"5")
False




>>> print("n">="h")
True




>>> print("n"<="h")
False




>>> print("110">"111")
False




>>> print("110"="111")
SyntaxError: keyword can't be an expression




>>> print("110"=="111")
False




>>> print("110"=="110")
True




>>> print("110"<"111")
True




>>> print("110">"5")
False




>>> print("110"<"5")
True




>>> print("111"<"110")
False




>>> print("111">"110")
True



>>> 10==10
True




>>> 11==10
False




>>> 10!=10
False




>>> 10!==10
SyntaxError: invalid syntax




>>> 10<>10
SyntaxError: invalid syntax




>>> "sps"=="sps"
True




>>> "sps"=="sp"
False
