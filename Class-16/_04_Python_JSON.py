"""
>> JSON

- JavaScript Object Notation
- It's a key value pair
- It's popular light-weight way of transferring data

This is one json with 5 fields each key value pair should be separated by comma
{
    "name" 		: "Anna",
    "age" 		: 18  ,
    "isMarried" : false ,
    "gender"	: "female",
    "company"	: null
}
"""

"""
>> Python JSON

- JSON is a syntax for storing and exchanging data.
- JSON is text, written with JavaScript object notation.
- Python has a built-in package called json, which can be used to work with JSON data.

String -> json.loads() -> Object
Object -> json.dumps() -> String

json loads -> returns an object from a string representing a json object.

json dumps -> returns a string representing a json object from an object.
"""

# Parse JSON - Convert from JSON to Python

import json

# some JSON:
x = '{ "name":"Hasan", "age":28, "city":"Dhaka"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])  # 28

# Convert from Python to JSON

import json

# a Python object (dict):
x = {
    "name": "Hasan",
    "age": 28,
    "city": "Dhaka"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)  # {"name": "Hasan", "age": 28, "city": "Dhaka"}

"""
You can convert Python objects of the following types, into JSON strings:

- dict
- list
- tuple
- string
- int
- float
- True
- False
- None
"""

"""
>> Format the Result

- The json.dumps() method has parameters to make it easier to read the result

Use the indent parameter to define the numbers of indents
"""

import json

x = {
    "name": "Hasan",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Mahmud", "Rhidoy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}

# use four indents to make it easier to read the result:
print(json.dumps(x, indent=4))

"""
{
    "name": "Hasan",
    "age": 30,
    "married": true,
    "divorced": false,
    "children": [
        "Mahmud",
        "Rhidoy"
    ],
    "pets": null,
    "cars": [
        {
            "model": "BMW 230",
            "mpg": 27.5
        },
        {
            "model": "Ford Edge",
            "mpg": 24.1
        }
    ]
}
"""

# Use the separators parameter to change the default separator:

import json

x = {
    "name": "Hasan",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Mahmud", "Rhidoy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}

# use . and a space to separate objects, and a space, a = and a space to separate keys from their values:
print(json.dumps(x, indent=4, separators=(". ", " = ")))

"""
{
    "name" = "Hasan". 
    "age" = 30. 
    "married" = true. 
    "divorced" = false. 
    "children" = [
        "Mahmud". 
        "Rhidoy"
    ]. 
    "pets" = null. 
    "cars" = [
        {
            "model" = "BMW 230". 
            "mpg" = 27.5
        }. 
        {
            "model" = "Ford Edge". 
            "mpg" = 24.1
        }
    ]
}
"""

# Order the Result

import json

x = {
    "name": "Hasan",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Mahmud", "Rhidoy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}

# sort the result alphabetically by keys:
print(json.dumps(x, indent=4, sort_keys=True))

"""
{
    "age": 30,
    "cars": [
        {
            "model": "BMW 230",
            "mpg": 27.5
        },
        {
            "model": "Ford Edge",
            "mpg": 24.1
        }
    ],
    "children": [
        "Mahmud",
        "Rhidoy"
    ],
    "divorced": false,
    "married": true,
    "name": "Hasan",
    "pets": null
}
"""
