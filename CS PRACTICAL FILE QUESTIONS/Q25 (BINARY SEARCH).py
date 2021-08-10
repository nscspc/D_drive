def binary_search(list,low,high,val):
    if high<low:
        return None
    else:
        midval=low+(high-low//2)

        if list[midval]>val:
            return binary_search(list,low,midval-1,val)
        elif list[midval]<val:
            return binary_search(list,midval+1,high,val)
        else:
            return midval

list=[10,20,30,40,50]
print(binary_search(list,0,4,40))
