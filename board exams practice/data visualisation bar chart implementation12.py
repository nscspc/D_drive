import matplotlib.pyplot as pl
import numpy as np
#data to plot
x=[2,4,7,8,10]
y=[7,8,5,4,2]

x2=[1,3,5,7,9]
y2=[7,8,2,4,2]
#plot
pl.bar(x,y,label="Bar1")
pl.bar(x2,y2,label="Bar2")
pl.title("Bar Graph \n with multiline title")
pl.legend()

pl.show()
