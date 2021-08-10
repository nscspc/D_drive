# Checking if File exist :-
'''
To avoid getting an error, you might want to check if the file exists
before you try to delete it.
'''
import os
if os.path.exists("todelete.txt"):
    os.remove("todelete.txt")
else:
    print("The file does not exist .")

#to delete the entire folder :-
if os.path.exists("myfolder"):
    os.rmdir("myfolder")
else:
    print("Directory does not exists .")
