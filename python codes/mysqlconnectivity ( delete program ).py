import mysql.connector as my

mydb=my.connect(host="localhost",user="root",passwd="naveen",database="ss")
mycursor=mydb.cursor()
mycursor.execute("delete from salary where staffid=336")
mydb.commit()

print("Data deleted Successfully")

