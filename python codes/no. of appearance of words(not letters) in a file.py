file=open("e:\\sps.txt","r")
str=" "
content=file.read()
words=content.split()#split function makes a list after separating the data read according to spaces and \n(enter).
x,i=0,0
for d in words:
    print(d)
#while(x<len(words)):
while(i<len(words)):
    a=0
    z=words[i]
    y=words.count(z)
    print("Appearance of","'",z,"'","is",y)
    while(a<y):
        words.remove(z)
        a=a+1
    #x=x+1
    
