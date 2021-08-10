import time
start=time.time()
s=0
for x in range(1,11):
    s=s+x
print("SUM is",s)
end=time.time()
t=end-start
print("Total TIME Taken :",t)
