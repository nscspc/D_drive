import mysql.connector as my

mydb=my.connect(host="localhost",user="root",passwd="manager")
mycursor=mydb.cursor()
mycursor.execute("create database employee")

print("database created successfully")
