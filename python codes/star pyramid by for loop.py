for x in range(1,5):
    for y in range(1,5-x):
        print(" ",end=" ")
    for z in range(1,x+1):
        print(" *",end=" ")
    print()
