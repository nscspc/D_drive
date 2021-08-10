# Python Try Except:-
'''
=> The try block lets you test a block of code for errors.
=> The except block lets you handle the error.
=> The finally block lets you execute code, regardless of the
    result of the try- and except blocks.
'''
# Exception Handling:-
'''
=>When an error occurs, or exception as we call it, Python will
    normally stop and generate an error message.
=> These exceptions can be handled using the try statement:
=> Example
    ->The try block will generate an exception, because x is not
       defined:
'''
try:
  print(x)
except:
  print("An exception occurred")

print()
print()

# Many Exception :-
'''
=> We can define as many exception blocks as we want .
'''
x=10
try:
    print(x/0)
except NameError:#it means that when NameError is going to occur then only this except block is going to execute
    print("Variable x is not defined")
except:# if NameError is not going to occur then , this except block is going to execute.
    print("Something else went wrong")

print()
print()

# else :-
'''
=> We can use the else keyword to define a block of code to be
    executed if no errors were raised.
'''
try:
    print("Hello")
except:
    print("Something went wrong")
else:# means else block is going to execute when except block is not going to execute.
    print("Nothting went wrong")

print()
print()

# finally :-
'''
=> The finally block , if specified , will be executed regardless if the
    try block raises an error or not.
'''
try:
    print(y)
except:
    print("Something went wrong")
finally:
    print("The 'try except' is finished")

'''
=> This can be useful to close objects and clean up resources:

=> Example
    -> Try to open and write to a file that is not writable:
--------------------------------------------
try:
  f = open("demofile.txt")
  f.write("Lorum Ipsum")
except:
  print("Something went wrong when writing to the file")
finally:
  f.close()
--------------------------------------------
'''
print()
print()
'''
# Raise an Exception :-

=> To throw(or raise) an exception , we can use 'raise' keyword .

x=-1
if x<0:
    raise Exception("Sorry , no numbers below zero")

print()
'''
    # we can also define what kind of error to raise, and the text to print to the user.
x="hello"
if not type(x) is int:
    raise TypeError("Only integers are allowed")

# we cannot raise 2 exception or errors in a single program.
