"""
A Python set is an unordered list of immutable elements. It means:
- Elements in a set are unordered.
- Dictionaries are used to store data values in key:value pairs.
- Creating a dictionary is as simple as placing items inside curly braces {} separated by commas.
"""

# Creating Python Dictionary

# empty dictionary
my_dict = {}

# dictionary with integer keys
my_dict = {1: 'apple', 2: 'ball'}
print(my_dict)  # {1: 'apple', 2: 'ball'}

# dictionary with mixed keys
my_dict = {'name': 'John', 1: [2, 4, 3]}
print(my_dict)  # {'name': 'John', 1: [2, 4, 3]}

# using dict()
my_dict = dict({1: 'apple', 2: 'ball'})
print(my_dict)  # {1: 'apple', 2: 'ball'}

# from sequence having each item as a pair
my_dict = dict([(1, 'apple'), (2, 'ball')])
print(my_dict)  # {1: 'apple', 2: 'ball'}

# Accessing Elements from Dictionary

# get vs [] for retrieving elements
my_dict = {'name': 'Hasan', 'age': 26}

print(my_dict['name'])
# Output: Hasan

print(my_dict.get('age'))
# Output: 26

# Trying to access keys which doesn't exist throws error
# Output None
print(my_dict.get('address'))

# KeyError
print(my_dict['address'])

# Changing and Adding Dictionary elements

# Changing and adding Dictionary Elements
my_dict = {'name': 'Hasan', 'age': 26}

# update value
my_dict['age'] = 27

print(my_dict)
# Output: {'age': 27, 'name': 'Hasan'}

# add item
my_dict['address'] = 'Dhaka'

print(my_dict)
# Output: {'address': 'Dhaka', 'age': 27, 'name': 'Hasan'}


# Removing elements from a dictionary

# create a dictionary
squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# remove a particular item, returns its value
print(squares.pop(4))
# Output: 16

print(squares)
# Output: {1: 1, 2: 4, 3: 9, 5: 25}

# remove an arbitrary item, return (key,value)
print(squares.popitem())
# Output: (5, 25)

print(squares)
# Output: {1: 1, 2: 4, 3: 9}

# remove all items
squares.clear()

# Output: {}
print(squares)

# delete the dictionary itself
del squares

# Throws Error
print(squares)

# Dictionary Methods
marks = {}.fromkeys(['Math', 'English', 'Science'], 0)

print(marks)
# Output: {'English': 0, 'Math': 0, 'Science': 0}

# Membership Test for Dictionary Keys
squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}

# Output: True
print(1 in squares)

# Output: True
print(2 not in squares)

# membership tests for key only not value
# Output: False
print(49 in squares)

"""
all()	    Return True if all keys of the dictionary are True (or if the dictionary is empty).
any()	    Return True if any key of the dictionary is true. If the dictionary is empty, return False.
len()	    Return the length (the number of items) in the dictionary.
cmp()	    Compares items of two dictionaries. (Not available in Python 3)
sorted()	Return a new sorted list of keys in the dictionary.
"""

# Dictionary Built-in Functions
squares = {0: 0, 1: 1, 3: 9, 5: 25, 7: 49, 9: 81}

print(all(squares))
# Output: False

print(any(squares))
# Output: True

print(len(squares))
# Output: 6

print(sorted(squares))
# Output: [0, 1, 3, 5, 7, 9]

keys = [1,2,3]
values = ['Value 1', 'Value 2', 'Value 3']

# zip function in dictionary
dict = dict(zip(keys, values))

# printing result
print(dict)  # {1: ‘Value 1’, 2: ‘Value 2’, 3: ‘Value 3’}
