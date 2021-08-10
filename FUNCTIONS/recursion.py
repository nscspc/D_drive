# recursion :-

def r(k):
    if(k>0):
        result=k+r(k-1)
        print(result)
    else:
        result=0
    return result

print("recursion example results : ")
r(6)
