l=["january","febuary","march","april","may","june","july","august","september","october","november","december"]
# program to find out DOB.
x=input("Does your birthday month lie in 1st half ? : ")
if x=="y":
    del l[6:12]
    
else:
    del l[1:6]
    
y=input("Does your birthday mnth lie in 1st 3 months ? : ")
if y=="y":
    del l[4:6]
else:
    del l[1:3]

b=0
while(b<3):
    print("Does your birth day month is",l[b],":")
    z=input("enter y/n : ")
    if z=="y":
        break
    else:
        b=b+1

c=l[b]
print(c)

x1=input("Does your birth date is in 1st half in the month ? : ")
y1=input("Does your birth date is even ? : ")

l1=[]
if x1=='y':
    a1=15
    no=1
else:
    a1=31
    no=15
    
while(no<=a1):
    if y1=='y':
        if no%2==0:
            l1.append(no)
    else:
        if no%2!=0:
            l1.append(no)
    no=no+1

print(l1)

if x1=='y':
    d1=input("does your birth date is single digit ? : ")
    if d1=="y":
        no1=3
        print("Does your birth date is divisible by",no1,":")
        z2=input("enter y/n : ")
        if z2=="y":
            print("is your birth date is",no1)
            i=input("enter y/n : ")
            
        else:
            b=b+1
