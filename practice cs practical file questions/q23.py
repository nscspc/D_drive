import random
var=True
while var:
    no=random.randint(1,6)
    guess=int(input("enter your guess : "))
    if no==guess:
        print("Congratulatons , you won a lottery")
        print("random no. was also :",no)
    else:
        print("Sorry , better luck next time")
        print("random no. was :",no)
    flag=0
    while(flag==0):
        choice=input("do you want to continue ? (y/n) : ")
        if choice=="y" or choice=="Y":
            var=True
            flag=1
        elif choice=="n" or choice=="N":
            var=False
            flag=1
            print("Thank You for playing !")
        else:
            print("invalid input")
        
