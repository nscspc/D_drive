print("dfsfasf".rsplit("s"))
print("dfsfasf".rsplit("f"))
print("df,sfa,sf".rsplit(":"))

grocery = "milk,chicken,bread,butter"#rsplit function does not works with whole list#
# specifying maxsplit value:
print(grocery.rsplit(',',2))#2=no. of value it is going to split from right side# 
print(grocery.rsplit(',',1))
print(grocery.rsplit(',',5))
print(grocery.rsplit(',',0))

'''
The split() method breaks up a string at the specified separator and returns a list of strings.

The syntax of split() is:

str.split([separator [, maxsplit]])

#split( ) is going to execute form left to right#
'''
