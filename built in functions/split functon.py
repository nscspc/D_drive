a="hello world"
b="hello,world"
print(a.split())
print(b.split(","))
print(b.split())
print(b.split(" "))
print(b.split("o"))

'''
output:

['hello', 'world']
['hello', 'world']
['hello,world']
['hello,world']
['hell', ',w', 'rld']

'''
