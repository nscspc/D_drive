import mysql.connector as my

mydb=my.connect(host="localhost",user="root",passwd="naveen",database="school")
mycursor=mydb.cursor()
mycursor.execute("create table student (RollNO int(5) primary key,Name varchar(50),age int(3),city char(8))")
print("table created successfully")
