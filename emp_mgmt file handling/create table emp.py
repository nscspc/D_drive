import mysql.connector as my

mydb=my.connect(host="localhost",user="root",passwd="manager",database="employee")
mycursor=mydb.cursor()
mycursor.execute("create table emp(id int(5),name varchar(50),salary int(10))")
mydb.commit() #:- no need of writting here.
print("table created successfully")
