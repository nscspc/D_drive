country={}
x=int(input("How many country details do you want to enter : "))
for i in range(0,x):
    con=input("enter country name : ")
    cap=input("enter country's capital : ")
    cur=input("enter country's currency : ")

    country[con]=[cap,cur]
    
for row in zip(*([key]+(value) for key ,value in sorted(country.items()))):
    print(*row)
    print()
