data=['D','o',' ','I','t',' ','@',' ','1','2','3',' ','!']

for i in range(len(data)-1):
    if (data[i].isupper()):
        data[i]=data[i].lower()
    elif (data[i].isspace()):
        data[i]=data[i+1]
print(data)
