country={}
n=int(input("how many country details do you want to enter : "))
m=0
while(m<n):
    con=input("enter country name : ")
    cap=input("enter country's capital : ")
    cur=input("enter country's currency : ")
    d={con:{"capital":cap,"currency":cur}}
    m=m+1
    country=country+d
for i in country:
    print("country",i,":")
    print("capital : ",str(d[i]["capital"]))
    print("currency : ",str(d[i]["currency"]))
