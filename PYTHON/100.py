#username
#first name , last name
#age
#18> adult
d={}

un=input("enter your user name : ")
fs=input("enter first name : ")
ls=input("enter last name : ")
age=int(input("enter your age : "))
d[un]={'first_name ': fs , 'last_name':ls,'age':age}

for un,ui in d.items():
    print(un)
    print()
    print(fs,ls)
    print(age)
    
#f=fopen("e://data.txt","a")
#fwritte
print(d)
