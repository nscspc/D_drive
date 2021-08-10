import matplotlib.pyplot as pl

a=[1,2,3]
x=[5,7,4]
pl.plot(a,x,label="first line")

b=[1,2,3]
y=[10,11,14]
pl.plot(b,y,label="second line")

pl.xlabel("plot no.")
pl.ylabel("imp. varaibles")
pl.title("new graph")

pl.legend()

pl.show()
