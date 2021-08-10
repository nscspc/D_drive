import mysql.connector as my

mydb=my.connect(host='localhost',user='root',password='manager',database='cs')
mycursor=mydb.cursor()
mycursor.execute('select distinct department from staff')
mydata=mycursor.fetchone()
for i in mydata:
    print(i)
