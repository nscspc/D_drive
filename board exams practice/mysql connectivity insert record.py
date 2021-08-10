import mysql.connector as my

mydb=my.connect(host="localhost",user="root",passwd="naveen",database="school")
mycursor=mydb.cursor()
mycursor.execute("insert into student values(2,'b',16,'jaipur',500,0000000001)")
mycursor.execute("insert into student values(3,'c',16,'jaipur',500,0000000002)")
mydb.commit()
print(mycursor.rowcount,"record inserted")
