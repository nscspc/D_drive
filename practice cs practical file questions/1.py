import mysql.connector as my
mydb=my.connect(host="localhost",user="root",passwd="manager")
mycursor=mydb.cursor()
mycursor.execute("show databases")
for i in mycursor:
    print(i)
