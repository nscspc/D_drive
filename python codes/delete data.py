import mysql.connector as my

mydb=my.connect(host="localhost",user="root",passwd="manager",database="employee")
mycursor=mydb.cursor()
mycursor.execute("delete from emp where name='a'")
mydb.commit()
print("data deleted successfully")
