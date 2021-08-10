import mysql.connector as my

mydb=my.connect(host="localhost",user="root",passwd="manager",database="employee")
mycursor=mydb.cursor()
mycursor.execute("update emp set name='b' where name='a'")
mydb.commit()
print("data updated successfully")
