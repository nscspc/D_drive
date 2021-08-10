import matplotlib.pyplot as pl
import numpy as np

x=np.linspace(1,5,4)# linspace() :- It generates linearly spaced vectors & gives direct control over the no. of points .
'''linspace(p,q,r) :-
   | p :- starting point |
   | q :- ending point   |
   | r :- no. of points on the line |'''
y=np.log(x)

pl.plot(x,y,"-+")

pl.show()
