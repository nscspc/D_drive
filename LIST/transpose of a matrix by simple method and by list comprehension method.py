#nrmal method
l=[[12,3,4],[5,6,7]]
print(l,"\n")
print(l[0])
print(l[1],"\n")
nl=[]
len=len(l[1])
for i in range(len):
    for j in l:
        nl.append(j[i])
    nl.append("\n")
for i in nl:
    print(i,end=" ")

#by list comprehension :-
nln=[[j[i] for j in l] for i in range(len)]
#nl2=[x[i] for i in range(len(l[1])) for x in l]
#nl3=[[x for x in l]  for i in range(len(l[1]))]
#print(nl2)
#print(nl3)
print(nln)

#another normal method
transposed=[]
matrix=[[1,2,3,4],[5,6,7,8]]
len=len(matrix[1])
for i in range(len):
    temp_mat=[]
    for j in matrix:
        temp_mat.append(j[i])
    transposed.append(temp_mat)
print(transposed)

'''
output:

[[1, 4], [2, 5], [3, 6], [4, 8]]

 # on online compiler it works
'''
