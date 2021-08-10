import matplotlib.pyplot as pl
#data to plot
labels=["Drinking",'Washing',"Cooking",'Bathing',"Toilet"]
sizes=[10,25,5,35,25]
color=['r','c','g','y','b']

#plot
pl.pie(sizes,labels=labels,colors=color,shadow=True,startangle=90)
pl.title("Consumption of Water in daily life")
pl.axis("equal")
pl.show()
