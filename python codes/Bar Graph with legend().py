import numpy as np
import matplotlib.pyplot as pl
x=[1,2,3,4]
y=[5,6,7,8]
x2=[2,3,4,5]
y2=[6,7,8,9]
pl.bar(x,y,color="blue",label="bar1")
pl.bar(x2,y2,color="orange",label="bar2")
pl.xlabel("x")
pl.ylabel("y")
pl.legend()
pl.show()
