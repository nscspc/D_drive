list=[1,5,3,7,6,4,2,6,4,6,55]
no=int(input("enter no. which you want to search :"))
for x in range(11):
    if list[x]==no:
        print(no,"found at",x,"position")
        break
