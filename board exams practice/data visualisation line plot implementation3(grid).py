import matplotlib.pyplot as pl
import numpy as np

x=np.arange(0.0,20.0,1)
a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
b=[4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]

pl.subplot(2,1,2) # SUBPLOT :- It is a function  which can be called to plot two or more plotsnin one figure.
'''| subplot(p,q,r) :- to plot diff. line in diff. graph  |
   | p,q :- dimensions of the graph of diff. lines      |
   | r :- no. of chart OR place of chart(1st or 2nd)  |
   | p & q should be same in both subplot function of both graphs |
   |& r shorld be different(if 2 graphs then r=1 or r=2 , if 3 graphs then r=1 or r=2 or r=3) if r is same then graph is made only one |'''
pl.plot(x,a)
pl.ylabel("value")
pl.title("first chart")
pl.grid(True)
# two subplotfunctions are used to plot two graphs in one figure
pl.subplot(2,1,1)
pl.plot(x,b)
pl.xlabel("item(s)")
pl.ylabel("value")
pl.title("\n\n second chart")
pl.grid(True)
pl.show()
