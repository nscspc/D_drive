import matplotlib.pyplot as pl

#data to plot
labels=['3-10yrs','11-18yrs','19-26yrs','27-34yrs','35-42yrs','42-49','50-58']
sizes=[1,3,5,7,9]

#plot
pl.bar(labels,sizes)
pl.title('Bar graph showing mostly affected age group from allergic rhinitis')
pl.xlabel("Age of patients")
pl.ylabel('No. of patients')
pl.show()
