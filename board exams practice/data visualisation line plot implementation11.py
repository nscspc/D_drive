import matplotlib.pyplot as pl
import numpy as np
#data to plot
labels=["python","c++","java","peri","scala","lisp"]
y=np.arange(len(labels))
sizes=[10,8,6,4,2,1]
#plot
pl.barh(y,sizes,color="orange")# in case of barh:-(y,x{size}) and in vase of vertical:-(x,y{size})
pl.yticks(y,labels)
pl.xlabel("performance")
pl.title("programming language usage")

pl.show()
