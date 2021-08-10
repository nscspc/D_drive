import matplotlib.pyplot as pl
import numpy as np

l=[89,99,95,90,89]
labels=["1st year","2nd year","3rd year","4th year","5th year"]

pl.bar(labels,l)
pl.title("SCHOOL RESULT of 5 CONSECUTIVE YEARS")
pl.xlabel("years")
pl.ylabel("result")
#pl.xlabels(labels)
pl.show()
