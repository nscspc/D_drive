import matplotlib.pyplot as pl
#data to plot
sizes=[]
labels=[]
color=[]
for i in range(5):
    x=input("Enter the Category : ")
    labels.append(x)
    y=int(input("Enter the consumption of water (in %) : "))
    sizes.append(y)
    z=input("Enter the colour : ")
    color.append(z)
    
#plot
pl.pie(sizes,labels=labels,colors=color)
pl.title("Consumption of Water in daily life")
pl.axis("equal")
pl.show()
