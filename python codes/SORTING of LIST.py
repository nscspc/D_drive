list=[53,76,35,4,43]
print("LIST elements BEFORE SORTING :",list)
for x in range(5):
    for y in range(x,5):
        if list[x]>list[y]:
            tmp=list[x]
            list[x]=list[y]
            list[y]=tmp
print("LIST elements AFTER SORTING :",list)
