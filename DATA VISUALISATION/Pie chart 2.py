import numpy as np
import matplotlib.pyplot as pl
# data to plot
labels=['Python','C++','Ruby','Java']
sizes=(215,130,245,210)
colors=('gold','yellowgreen','lightcoral','lightskyblue')
explode=[0.1,0,0,0] # explode lst slice

# plot
pl.pie(sizes,explode=explode,labels=labels,colors=colors,shadow=False,startangle=90)
pl.axis('equal')
pl.title("Popular Languages among the Students")
pl.show()
