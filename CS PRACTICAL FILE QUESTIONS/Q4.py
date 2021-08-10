num1=float(input("enter number 1 : "))
num2=float(input("enter number 2 : "))
num3=float(input("enter number 3 : "))
if num1>num2 and num1>num3:
    print("the first number is greater")
elif num2>num1 and num2>num3:
    print("the second number is greater")
elif num3>num1 and num3>num1:
    print("the third number is greater")
else:
    print("All numbers are equal")
