# Python Delete File:-
'''
to delete a file, we must import the os module , and run its
os.remove( ) function .
'''
file=open("todelete.txt","w")
file.close()#we have to first of all close the file before deleting it , or doing another process on it.
import os
os.remove("todelete.txt")
