lst=[11,24,76,5,78,98,456,23,54]
p=len(lst)
no=int(input("Enter no. which you want to search"))
for x in range(p):
    if lst[x]==no:
        print(no,"found at",x,"position")
        break
