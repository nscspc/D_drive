import matplotlib.pyplot as pl
import numpy as np
#data to plot
labels=["1st Year","2nd Year","3rd Year","4th Year","5th Year"]
sizes=[]
for i in range(1,6):
    x=int(input("Enter the Result of consecutive year : "))
    sizes.append(x)
y=np.arange(len(labels))# it specifies the numerical value of the point  on the x-axis according to the length of the list.
# at the place of 'len(labels)' we can put 5 also as both are same.
pl.bar(y,sizes)# in bar() :- we should necessarily put data of x-axis(specificatin of no. of bars) and yaxis(sizes of bars) , and we can also put color=color/colors,width,etc.
pl.xlabel("years")
pl.ylabel("results")
pl.xticks(y,labels)#for labelling the bars at the x-axis using ticks()
pl.title("Result of School for 5 Consecutive Years")
pl.show()
