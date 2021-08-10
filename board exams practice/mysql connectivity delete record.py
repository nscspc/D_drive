import mysql.connector as my

mydb=my.connect(host="localhost",user="root",passwd="naveen",database="school")
mycursor=mydb.cursor()
mycursor.execute("delete from student where rollno=1")
mydb.commit()
print(mycursor.rowcount,"records deleted")
