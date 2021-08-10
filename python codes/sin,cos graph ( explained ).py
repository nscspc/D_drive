# importing libraries
import numpy
import matplotlib.pyplot

# defining coordinates for plotting graph ( using numpy library )
x=numpy.arange(5.,20,2.5) # 5/5.=starting point , 20=ending point , 2.5=distance( A/C t x-axis ) b/w 2 points
a=numpy.cos(x) # cos wali graph
b=numpy.sin(x) # sin wali graph

# code for plotting graph using the coordinates which we have defined above ( using matplotlib.pyplot )
matplotlib.pyplot.plot(x,a,"b") # in this x is used for arranging the graph & a is usedd for plotting cos graph  A/C to x & "b" is color
matplotlib.pyplot.plot(x,b,"r") # in this x is used for arranging the graph & b is usedd for plotting cos graph  A/C to x & "r" is color

# to show the graph
matplotlib.pyplot.show()
