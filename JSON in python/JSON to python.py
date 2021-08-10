# JSON :-
'''
=> JSON is a syntax for storing and exchanging data.
=> JSON is text , written with JavaScript Object Notation(json).
'''

# Python has a built-in package called json , which can be used to work with JSON data.
'''
import json
'''

# parse JSON - Converting from JSON to Python.
import json

    #JSON data:-
x='{"name":"John","age":30,"city":"New York"}'

    #parse x:-
y=json.loads(x)

    #the result is a Python Dictionary:-
print(y["age"])
