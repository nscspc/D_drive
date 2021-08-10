import mysql.connector as my

mydb=my.connect(host="localhost",user="root",passwd="naveen",database="school")
mycursor=mydb.cursor()
mycursor.execute("select*from student")
myrecords=mycursor.fetchall()
for x in myrecords:
    print(x)
