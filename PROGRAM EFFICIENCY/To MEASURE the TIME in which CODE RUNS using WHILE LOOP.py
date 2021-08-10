import time
start=time.time()
s=0
x=1
while(x<=10):
    s=s+x
    x=x+1
print("SUM is",s)
end=time.time()
t=end-start
print("Total TIME Taken :",t)
