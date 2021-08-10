n=int(input('how many students?'))
compwinners={}
for a in range(n):
    key=input('name of the student :')
    value=int(input('number of competitions won :'))
    compwinners[key]=value
print('the dictionary now is :')
print(compwinners)
