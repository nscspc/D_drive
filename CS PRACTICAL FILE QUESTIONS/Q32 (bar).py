import numpy as np
import matplotlib.pyplot as pl
# data to be enter by the user
a=0
s=list()
while(a<5):
    x=int(input("Enter the Result of Consecutive Year"))
    s.append(x)
    a=a+1
# data to plot
labels=('1st Year','2nd Year','3rd Year','4th Year','5th Year')
x=np.arange(len(labels))
siz=s
colors=("green","red","blue","yellow","orange")

# plot
pl.bar(x,siz,color=colors)
pl.xticks(x,labels)
pl.ylabel("result")
pl.title("The Result of School for 5 Consecutive Years")
pl.show()
