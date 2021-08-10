#isidentifier( ) :- this function returns true if the string can be a (identifier) or a name of anything that can be created (keywords are also included), false if it is not valid in python
x="a"
print(x.isidentifier())
print(">".isidentifier())
print("_".isidentifier())
print(".".isidentifier())
print("int".isidentifier())
