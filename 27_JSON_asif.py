# JSON

import json

# Parse JSON - Convert from JSON to Python

x =  '{ "name":"John", "age":30, "city":"New York"}'  # some JSON:

y = json.loads(x)  # parse x:

print(y["age"])   # the result is a Python dictionary:

# Convert from Python to JSON

x = {
  "name": "John",
  "age": 30,
  "city": "New York"
} # a Python object (dict):


y = json.dumps(x)  # convert into JSON:


print(y) # the result is a JSON string:

# Another example

# dict
print(json.dumps({"name": "John", "age": 30}))

# list
print(json.dumps(["apple", "bananas"]))

# tuple
print(json.dumps(("apple", "bananas")))

# string
print(json.dumps("hello"))

# int
print(json.dumps(42))

# float
print(json.dumps(31.76))

# True
print(json.dumps(True))

# False
print(json.dumps(False))

# None
print(json.dumps(None))

# Another example

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

# Format the Result

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

print(json.dumps(x, indent=4)) # use four indents to make it easier to read the result:

# Another example

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

print(json.dumps(x, indent=4, separators=(". ", " = "))) # use . and a space to separate objects, and a space, a = and a space to separate keys from their values

# Order the Result

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

print(json.dumps(x, indent=4, sort_keys=True)) # sort the result alphabetically by keys

# 