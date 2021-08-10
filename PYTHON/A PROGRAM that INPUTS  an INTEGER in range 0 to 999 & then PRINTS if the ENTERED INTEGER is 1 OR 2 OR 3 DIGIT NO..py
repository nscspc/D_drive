x=int(input("enter no."))
if x>=0 and x<=999:
    if x>=0 and x<10:
        print("1 digit no.")
    elif x>=10 and x<=99:
        print("2 digit no.")
    else:
        print("3 digit no.")
else:
    print("OUT of RANGE")
