import time
#binary search : list should be in ascending order
t1=time.time()
def bs(list,low,high,value):
    if high<low:
        return None
    midval=low+((high-low)//2)
    if list[midval]>value:
        return bs(list,low,high-1,value)
    elif list[midval]<value:
        return bs(list,low+1,high,value)
    else:
        return midval
list=[1,4,5,8,10,44]
print(bs(list,2,5,10))
t2=time.time()
t=t2-t1
print(t)
