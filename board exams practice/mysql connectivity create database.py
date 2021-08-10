import mysql.connector as my

mydb=my.connect(host="localhost",user="root",passwd="naveen")
mycursor=mydb.cursor()
mycursor.execute("create database school")
print("database create successfully")
