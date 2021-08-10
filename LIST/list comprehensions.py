#normal
cube=[]
for i in range(1,11):
    cube.append(i**3)
print(cube)

#list comprehensions
cube=[i**3 for i in range(1,11)]
print(cube)
