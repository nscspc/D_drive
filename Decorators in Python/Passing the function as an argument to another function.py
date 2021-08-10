# Passing the function as argument :-

def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

def greet(func):
    greeting=func("Hi, I am created by a function passed as an argument.")
    print(greeting)

greet(shout)
greet(whisper)

'''
In the above example, the greet function takes another function
as a parameter (shout and whisper in this case). The function
passed as argument is then called inside the function greet.
'''
