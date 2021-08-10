Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("hello")
hello




>>> print('hello')
hello




>>> print(hello)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    print(hello)
NameError: name 'hello' is not defined




>>> hello
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    hello
NameError: name 'hello' is not defined




>>> "hello"
'hello'




>>> print(4655+465465)
470120




>>> 4655+465465
470120




>>> print("4655"+"465465")
4655465465




>>> print"hello"
SyntaxError: invalid syntax




>>> "4655"+"465465"
'4655465465'




>>> x=4
>>> y=8
>>> z=x+y
>>> z
12
>>> print(z)
12




>>> x=10
>>> print(z)
12



 
>>> x=10
>>> y=10
>>> z=x+y
>>> z
20




>>> y=20
>>> z
20




>>> x=8
>>> x=4
>>> y=10
>>> z=x+y
>>> z
14




>>> a=4
>>> a+4
8




>>> a+4,a-2
(8, 2)




>>> (a+4,a-2)
(8, 2)




>>> [a+4,a-2]
[8, 2]




>>> {a+4,a-2}
{8, 2}




>>> |a+4,a-2|
SyntaxError: invalid syntax




>>> "a+4,a-2"
'a+4,a-2'




>>> "a+4","a-2"
('a+4', 'a-2')




>>> print("a+4","a-2")
a+4 a-2




>>> print("a+4,a-2")
a+4,a-2




>>> print(a+4,a-2)
8 2




>>> a+4,a-2
(8, 2)




>>> 10+10
20




>>> hello+india
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    hello+india
NameError: name 'hello' is not defined




>>> "hello+india"
'hello+india'




>>> "hello"+"india"
'helloindia'




>>> ("hello"+"india")
'helloindia'




>>> print("hello"+"india")
helloindia




>>> 10+4
14




>>> 10-5
5




>>> 10/5
2.0




>>> 10\5
SyntaxError: unexpected character after line continuation character




>>> 10/3
3.3333333333333335





>>> 10//3
3




>>> 10*10
100




>>> 10**10
10000000000





>>> 10%3
1




>>> 10/2*3+4-1
18.0




>>> 1-4+3*2/10
-2.4




>>> 1-4/4+1*7
7.0




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




 
