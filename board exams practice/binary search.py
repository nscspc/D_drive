def bs(l,low,high,val):
    if high<low:
        return None
    else:
        midval=low+high//2
    if l[midval]>val:
        return(bs(l,low,high-1,val))
    elif l[midval]<val:
        return(bs(l,low+1,high,val))
    else:
        return midval

l=[0,1,2,3,6,78,91,500]# list should be in ascending(sorted) order 
print(bs(l,0,len(l)-1,500))
