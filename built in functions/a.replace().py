a="adda"

#1
print(a.replace("a","v"))
#output:
#    vddv

#2
print(a.replace("a[0]","v"))
#output:
#    adda

#3
print(a.replace("[0]","v"))
#output:
#    adda

#4
print(a.replace("ad","vd"))
#output:
#    vdda

#5
print(a.replace("ad","v"))
#output:
#    vda

#6
print(a.replace("a","vd"))
#output:
#    vdddvd
