import mysql.connector as my

mydb=my.connect(host='localhost',user='root',password='manager')
mycursor=mydb.cursor()
mycursor.execute('create database pm')
print('database successfully created')
