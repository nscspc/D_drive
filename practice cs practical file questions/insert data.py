import mysql.connector as my

mydb=my.connect(host='localhost',user='root',password='manager',database='cs')
mycursor=mydb.cursor()
mycursor.execute('insert into staff values(2,"0","0","0",0)')#at the place of (') we can also use (") or vice versa
mydb.commit()
print('data  inserted successfully')
