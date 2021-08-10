x="qwerty1234"
#1
print(x.endswith("34"))
print(x.endswith("123"))
print(x.startswith("q"),"\n\n")

#2
text="python programming is easy to learn."
result=text.endswith("learn.",7)
# start parameter: 7
# "programming is easy to learn." string is searched
print(result)

result=text.endswith("is",7,26)
# Both start and end is provided
# start: 7, end: 26
# "programming is easy" string is searched
print(result)

result=text.endswith("easy",7,26)
print(result,"\n\n")

#3 : endswith() With Tuple Suffix

'''
Passing Tuple to endswith()
It's possible to pass a tuple suffixes to the endswith() method in Python.

If the string ends with any item of the tuple, endswith() returns True. If not, it returns False
'''
text = "programming is easy"
result = text.endswith(('programming', 'python'))

# prints False
print(result)

result = text.endswith(('python', 'easy', 'java'))

#prints True
print(result)

# With start and end parameter
# 'programming is' string is checked
result = text.endswith(('is', 'an'), 0, 14)

# prints True
print(result,"\n\n")


'''
The endswith() method returns True if a string ends with the specified suffix. If not, it returns False.

The syntax of endswith() is:

str.endswith(suffix[, start[, end]])


endswith() Parameters
The endswith() takes three parameters:

suffix - String or tuple of suffixes to be checked
start (optional) - Beginning position where suffix is to be checked within the string.
end (optional) - Ending position where suffix is to be checked within the string.


Return Value from endswith()
The endswith() method returns a boolean.

It returns True if strings ends with the specified suffix.
It returns False if string doesn't end with the specified suffix.

'''
