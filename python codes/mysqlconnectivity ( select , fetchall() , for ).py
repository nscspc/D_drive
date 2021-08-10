import mysql.connector as my

mydb=my.connect(host="localhost",user="root",passwd="manager",database="ss")
mycursor=mydb.cursor()
mycursor.execute("select * from salary where staffid=366")
row=mycursor.fetchall()

for i in row:
    print(i)
