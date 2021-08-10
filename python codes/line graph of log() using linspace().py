import numpy as np
import matplotlib.pyplot as pl

x=np.linspace(2,5,3) # linspace = it generates lineaarly spaced vectors & gives direct control over the no. of points , 2=starting point , 5=ending point , 3=no. of points(coordinates) A/C to which graph is to be plot
y=np.log(x) # log graph
pl.plot(x,y)
pl.show()
