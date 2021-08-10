import mysql.connector as my

mydb=my.connect(host="localhost",user="root",passwd="naveen",database="school")
mycursor=mydb.cursor()
mycursor.execute("alter table student add(phoneno int(10))")
print("column added successfully")
