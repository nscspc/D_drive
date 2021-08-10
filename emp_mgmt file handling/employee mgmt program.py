import mysql.connector as my
def search():
    s=input("enter name : ")
    mydb=my.connect(host="localhost",user="root",passwd="manager",database="employee")
    mycursor=mydb.cursor()
    mycursor.execute("select * from emp where name='"+s+"'")
    row=mycursor.fetchall()
    for i in row:
        print("id name salary")
        print(i,end=" ")

def alldata():
    mydb=my.connect(host="localhost",user="root",passwd="manager",database="employee")
    mycursor=mydb.cursor()
    mycursor.execute("select * from emp")
    row=mycursor.fetchall()
    print("id name salary")
    for i in row:
        print(i)

def adddata():
    eid=input("enter employee id : ")
    name=input("enter employee name : ")
    salary=input("enter employee salary : ")
    mydb=my.connect(host="localhost",user="root",passwd="manager",database="employee")
    mycursor=mydb.cursor()
    mycursor.execute("insert into emp values('"+eid+"','"+name+"','"+salary+"')") 
    mydb.commit()
    print("data added successfully")

def delete():
    eid=input("enter id of the employee whose record you want to delete : ")
    mydb=my.connect(host="localhost",user="root",passwd="manager",database="employee")
    mycursor=mydb.cursor()
    mycursor.execute("delete from emp where id='"+eid+"'")
    mydb.commit()
    print("data deleted successfully")

def update():
    eid=input("enter id of the employee of whose record you want to update : ")
    mydb=my.connect(host="localhost",user="root",passwd="manager",database="employee")
    mycursor=mydb.cursor()
    mycursor.execute("select * from emp where id='"+eid+"'")
    row=mycursor.fetchall()
    for i in row:
        print("id name salary")
        print(i,end=" ")
    ch=input("what do you want to update enter i (for id) , n (for name) , s (for salary) : ")
    if(ch=='i'):
        uid=input("enter new id : ")
        mycursor.execute("update emp set id='"+uid+"' where id='"+eid+"'")
        mydb.commit()
        print("data updated successfully")
    elif(ch=='n'):
        name=input("enter new name : ")
        mycursor.execute("update emp set name='"+name+"' where id='"+eid+"'")
        mydb.commit()
        print("data updated successfully")
    elif(ch=='s'):
        salary=input("enter new salary : ")
        mycursor.execute("update emp set salary='"+salary+"' where id='"+eid+"'")
        mydb.commit()
        print("data updated successfully")
    else:
        print("invalid input")

x=0
while(x<1):
    print("\n1. search record.\n2. see all records.\n3. add data.\n4. delete record.\n5. update data.\n6. exit")
    ch=int(input("enter choice : "))
    if(ch==1):
        search()
    elif(ch==2):
        alldata()
    elif(ch==3):
        adddata()
    elif(ch==4):
        delete()
    elif(ch==5):
        update()
    elif(ch==6):
        x=1
    else:
        print("invalid input")
        
