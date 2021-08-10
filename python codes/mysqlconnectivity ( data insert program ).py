import mysql.connector as my

mydb=my.connect(host="localhost",user="root",passwd="naveen",database="ss")
mycursor=mydb.cursor()
mycursor.execute("insert into salary values(366,15000,50000,1000)")
mydb.commit()

print("data inserted successfully")
