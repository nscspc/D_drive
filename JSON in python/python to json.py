# Converting from python to json:-
import json

    #a python object(dictionary):-
x={
    "name":"john",
    "age":30,
    "city":"New York"
    }

    #convert into JSON:-
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))
'''
When you convert from Python to JSON, Python objects are converted into the JSON (JavaScript) equivalent:

Python	JSON
dict	Object
list	Array
tuple	Array
str	String
int	Number
float	Number
True	true
False	false
None	null

'''
print()
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))
print()

#Format the Result:-
'''
=> The example above prints a JSON string,but it is not very
    easy to read, with no indentations and line breaks.
=> The json.dumps() method has parameters to make it easier
    to read the result.
'''
print(json.dumps(x,indent=4))
print()

#Changing the separators:-
'''
You can also define the separators, default value is (", ", ": "),
which means using a comma and a space to separate each object,
and a colon and a space to separate keys from values:
'''
print(json.dumps(x,indent=4,separators=(". "," = ")))
print()

#Order the Result:-
'''
=> The json.dumps() method has parameters to order the keys
    in the result:

=> Use the sort_keys parameter to specify if the result should
    be sorted or not:
'''
print(json.dumps(x, indent=4, sort_keys=True))
