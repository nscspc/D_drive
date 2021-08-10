import random
var=True
while var:
    flag=0
    no=random.randint(1,10)
    guess=int(input("enter your no. : "))
    if no==guess:
        print("congtrats")
    else:
        print("sorry")
    print("random no. was :",no)
    while(flag==0):
        choice=input("Do you want to play again ? Y/N : ")
        if choice=="y" or choice=="Y":
            var=True
            flag=1
        elif choice=="n" or choice=="N":
            var=False
            flag=1
        else:
            print("Invalid input.....Please enter correct input { Y/N }")
        
