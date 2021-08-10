print("affaf".partition("f"))
print("affaf".partition("a"))

string="python is fun"

#if separator not found then : the string itself and 2 empty strings are formed as 3 elements of a tuple#
print(string.partition('not'))

#if separator is found then : the string before , separator , the string after the separator are made as 3 elements of the tuple #
print(string.partition("is"))

#it splits the string at the first occurence of the separator#
print("affaf".partition("f"))
print("affaf".partition("a"))

'''
The partition() method splits the string at the first occurrence of the argument string and returns a tuple containing the part the before separator, argument string and the part after the separator.

The syntax of partition() is:

string.partition(separator)

'''
