import numpy as np
import matplotlib.pyplot as pl
# data to plot
labels=['Better 70%','Relieved 20%','Status Quotient 10%']
sizes=(70,20,10)
colors=('black','grey','white')
#explode=[0.1,0,0,0] # explode lst slice

# plot
pl.pie(sizes,labels=labels,colors=colors,startangle=90,autopct='%1.1f')
pl.axis('equal')
#pl.title("Popular Languages among the Students")
pl.show()
