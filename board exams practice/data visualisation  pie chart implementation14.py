import matplotlib.pyplot as pl

#data to plot
labels=["Python","C++","Ruby","Java"]
sizes=[215,130,254,210]
colors=["gold","yellowgreen","lightcoral","lightskyblue"]
explode=[0.1,0,0,0]

#plot
pl.pie(sizes,labels=labels,explode=explode,colors=colors,shadow=True,startangle=140)#startangle:-distance b/w starting point ofgraph to 90 degree.
pl.axis("equal")

pl.show()
