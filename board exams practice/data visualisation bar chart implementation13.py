import matplotlib.pyplot as pl
import numpy as np
#data to plot
labels=["Comedy","Action","Romance","Drama","SciFi"]
x=np.arange(len(labels))
sizes=[4,5,6,1,4]

#plot
pl.bar(x,sizes)
pl.xticks(x,labels)
pl.ylabel("People")
pl.title("Favourite Type of Movie")

pl.show()

