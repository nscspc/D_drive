import mysql.connector as my

mydb=my.connect(host="localhost",user="root",passwd="manager",database="employee")
mycursor=mydb.cursor()
mycursor.execute("insert into emp values(1,'a',10000)")
mydb.commit()
print("data added successfully")
