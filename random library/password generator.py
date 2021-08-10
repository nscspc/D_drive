#password generator

import random
import pyfiglet
#print(random.randint(int(chr(65)),int(chr(2))))

letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
lnew=[]
for i in letters:
    lnew.append(i)
    lnew.append(i.upper())

n=[1,2,3,4,5,6,7,8,9,0]
symbols=['!','@','#','$','%','^','&','*','+','-','(']
logo=pyfiglet.figlet_format("password generator")#pyfiglet library contains a function figlet_format("string") which prints a patten in big size of the entered string . 
print(logo)

ls=int(input("no. of letters : "))
ns=int(input("no. of numbers : "))
ss=int(input("no. of symbols : "))

pswd=[]

for i in range(ls):
    letter=random.choice(lnew)
    pswd+=letter

for i in range(ns):
    letter=random.choice(n)
    pswd+=str(letter)

for i in range(ss):
    letter=random.choice(symbols)
    pswd+=letter

random.shuffle(pswd)#to use shuffle( ) function pswd(argument) should be a sequence(eg: list) 
pswd="".join(pswd)
print("\n generated password : "+pswd)

