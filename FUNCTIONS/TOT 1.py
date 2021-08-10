x=int(input("enter no."))
if(x<100 and x>0):
    if x%3==0:
        print("Fizz")
    if x%5==0:
        print("Buzz")
    if x%3==0 and x%5==0:
        print("FizzBuzz")
    else:
        print("it is not multiple of 3 or 5")
