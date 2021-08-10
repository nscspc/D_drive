import matplotlib.pyplot as pl

def fnplot(list1):
    pl.plot(list1)
    pl.title("marks line chart")
    pl.xlabel("value")
    pl.ylabel("frequency")
    pl.show()

list1=[50,50,50,65,65,7,5,0,80,90,90,90]
fnplot(list1)
# |values on x-axis represents indexes of list   |
# |& values on y-axis represents values of list1 |
