import matplotlib.pyplot as pl
#data to plot
sizes=[]
labels=[]
color=[]
explode=[]
colors=['g','b','y','orange','r']
explodes=[0,0,0,0,0.1]
for i in range(5):
    x=input("Enter the Category : ")
    labels.append(x)
    y=int(input("Enter the consumption of water (in %) : "))
    sizes.append(y)
a=sizes
for i in range(5):
    for k in range(i,5):
        if a[i]>a[k]:
            tmp=a[i]
            a[i]=a[k]
            a[k]=tmp
print(a)
print(sizes)
for z in range(5):
    for w in range(z,5):
        if a[z]==sizes[w]:
            color.insert(w,colors[z])
            explode.insert(w,explodes[z])
print(color)
print(explode)
#plot
pl.pie(sizes,labels=labels,colors=color,explode=explode,startangle=120,shadow=True)
pl.title("Consumption of Water in daily life")
pl.axis("equal")
pl.show()
