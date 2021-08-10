import matplotlib.pyplot as pl

#data to plot
sizes=[90,60,40]
labels=["better90%","relieved60%","status quotient40%"]
#color=["lightgreen","orange","blue","pink","brown"]

#title=input("enter title of pie chart : ")
#n=int(input("enter no. of data value you want to enter : "))

'''for i in range(1,n+1):
    if(i==2):
        j=str(i)+'nd'
    elif(i==3):
        j=str(i)+'rd'
    elif(i==1):
        j=str(i)+'st'
    else:
        j=str(i)+'th'
        
    labels.append(input("enter '"+j+"' label : "))
    sizes.append(float(input("enter '"+j+"'value : ")))
    color.append(input("enter colour : "))
'''
#plot
pl.pie(sizes,labels=labels)
#pl.title("outcome of medication in cases of Allergic rhinitis represented by pie chart")
#pl.legend()
pl.show()
