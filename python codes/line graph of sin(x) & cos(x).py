import numpy as np
import matplotlib.pyplot as pl

x=np.arange(0.,10,0.1)

a=np.cos(x)
b=np.sin(x)

pl.plot(x,a,'b')
pl.plot(x,b,'r')

pl.show()
