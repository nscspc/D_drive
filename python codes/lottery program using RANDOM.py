import random
var=True
while var:
    ch=random.randint(1,6)
    guess=int(input("Enter any No. : "))
    if ch==guess:
        print("CONGRATULATIONS you have WON a Lottery")
    else:
        print("Better Luck next time")
    print("Random No. was :",ch)
    choice=input("Do you want to Continue ? Y/N : ")
    if choice=="y" or choice=="Y":
        var=True
    else:
        var=False
