# find( ) :- this function searhes the string for a specified value and returns the position of where it was found # 
x="ab c asdf adf"
print(x.find("ab"))
print(x.find("c"))
print(x.find(" "))
print(x.find(" "))
print(x.find("df"))
print(x.find("as"))
print(x.find("i"))#find returns -1 if substring not found

#to solve above problem
#right way to use find( ):
if(x.find("i")!=-1):
    print("x contains substring 'i'")
    #/' this escape sequence is used when we have to store string with ' in a variable#
else:
    print("x doesn't contains substring 'i'")

'''
The find() method returns the index of first occurrence of the substring (if found). If not found, it returns -1.

The syntax of the find() method is:

str.find(sub[, start[, end]] )


Parameters for the find() method
The find() method takes maximum of three parameters:

sub - It is the substring to be searched in the str string.
start and end (optional) - The range str[start:end] within which substring is searched.


Return Value from find() method
The find() method returns an integer value:

If the substring exists inside the string, it returns the index of the first occurence of the substring.
If substring doesn't exist inside the string, it returns -1.

'''
