import numpy as np
import matplotlib.pyplot as pl
a=["FA-1","FA-2"]
b=[20,49]
c=np.arange(len(a))
pl.barh(c,b)
pl.yticks(c,a)
pl.xlabel("exam")
pl.ylabel("marks")
pl.show()
