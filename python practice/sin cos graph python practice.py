import numpy
import matplotlib.pyplot

#defining coordinates
x=numpy.arange(1,20,.1)
a=numpy.cos(x)
b=numpy.sin(x)

#plotting
matplotlib.pyplot.plot(x,a)
matplotlib.pyplot.plot(x,b)

#to show the graph
matplotlib.pyplot.show()
