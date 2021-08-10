import mysql.connector as my

mydb=my.connect(host="localhost",user="root",passwd="naveen",database="school")
mycursor=mydb.cursor()
mycursor.execute("update student set rollno=1 where rollno=2")
mydb.commit()
print(mycursor.rowcount,"records updated")
