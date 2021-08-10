# fetching information from a xcbd website:-

# API :- Application Programming Interface.
'''
API is the messenger between client and the server like the waiter between customer and chef.

TYPES OF API's:-
(1). Rest API => 3rd party API
(2). Soap API
(3). GraphQL API => developed by facebook

There is also API KEY :- it is a secret code , it is used to
track and monitor the request , and limited no. of request can be sent to the server

'''
import requests# request package allows us to make http/https request to get information from a website.,it is the most downloaded package.
r=requests.get("https://xkcd.com/353/")#we are doing the get(vulnerability) request . # website link.

print(r)#we get a response out of this link , means that the request is successful.
print(dir(r))#dir function tells us the methods available with the request module.
print(help(r))#using help method we will ger detailed info about methods.
print(r.text)#text method returns the html code of the page we are requesting.

print()
print()

r2=requests.get("https://imgs.xkcd.com/comics/python.png")#image link
print(r2)
print(r2.text)#text method shows the image in bytes format.
print(r2.content)#content method shows the hexadecimal code of the image.

print()

#now we have to save the image in the file in same directory as of python program.
with open("comic.png","wb") as f:
    f.write(r2.content)#to download file



#from datatime import datetime

#api_key='c73a53a3c2deb89ee1c27cc188a9f22b'
#location=input("enter city name : ")
