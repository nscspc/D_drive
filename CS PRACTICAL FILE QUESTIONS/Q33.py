import numpy as np
import matplotlib.pyplot as pl
# data to plot
labels=['Washing Clothes','Bathing','Drinking','Toilet','Cooking','Other']
sizes=(20,20,25,20,10,5)
colors=('gold','yellowgreen','lightcoral','lightskyblue','red','orange')
explode=[0,0,0.1,0,0,0] # explode lst slice

# plot
pl.pie(sizes,explode=explode,labels=labels,colors=colors,shadow=False,startangle=90)
pl.axis('equal')
pl.title("Consumption of WATER in Daily Life")
pl.show()
