import matplotlib.pyplot as pl
import numpy as np

x=np.arange(1,3)

pl.plot(x,"w")
pl.plot(x+1,"r")
pl.plot(x+2,"c")
''' colors :
| b(blue) , c(cyan) , g(green) , k(black) , m(magenta) , r(red) , w(white) , y(yellow) |''' 
pl.show()
