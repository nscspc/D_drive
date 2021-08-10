import mysql.connector as my

mydb=my.connect(host="localhost",user="root",passwd="naveen")
mycursor=mydb.cursor()
mycursor.execute("show databases")
for x in mycursor:
    print(x)
