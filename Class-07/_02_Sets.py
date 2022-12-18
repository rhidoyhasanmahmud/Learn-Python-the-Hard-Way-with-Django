"""
- Sets are used to store multiple items in a single variable.
- A set is a collection which is unordered, unchangeable*, and unindexed.

Note: Set items are unchangeable, but you can remove items and add new items.
"""
# To create a empty set you have to use the built-in method:
my_set = set()
print(my_set)  # set()

int_set = {1, 3, 2, 5, 3, 6}
print(int_set)  # {1, 2, 3, 5, 6}

# Type check
print(type(int_set))  # <class 'set'>

# Set Items - Data Types
## Set items can be of any data type.

mix_set = {"Python", 34, True, 40.5, "Java"}
print(mix_set)  # {True, 34, 'Python', 40.5, 'Java'}

# set cannot have duplicates
my_set = {1, 2, 3, 4, 3, 2}
print(my_set)
# Output: {1, 2, 3, 4}

# we can make set from a list
my_set = set([1, 2, 3, 2])
print(my_set)
# Output: {1, 2, 3}

# set cannot have mutable items
# here [3, 4] is a mutable list
# my_set = {1, 2, [3, 4]}  # TypeError: unhashable type: 'list'
# this will cause an error..

## Modifying a set in Python

# initialize my_set
my_set = {1, 3}
print(my_set)

# my_set[0]
# if you uncomment the above line
# you will get an error
# TypeError: 'set' object does not support indexing

# add an element
my_set.add(2)
print(my_set)
# Output: {1, 2, 3}

# add multiple elements
my_set.update([2, 3, 4])
print(my_set)
# Output: {1, 2, 3, 4}

# add list and set
my_set.update([4, 5], {1, 6, 8})
print(my_set)
# Output: {1, 2, 3, 4, 5, 6, 8}

## Removing elements from a set

"""
- discard() function leaves a set unchanged if the element is not present in the set.
- remove() function will raise an error in such a condition (if element is not present in the set).
"""

# initialize my_set
my_set = {1, 3, 4, 5, 6}
print(my_set)

# discard an element
my_set.discard(4)
print(my_set)
# Output: {1, 3, 5, 6}

# remove an element
my_set.remove(6)
print(my_set)
# Output: {1, 3, 5}

# discard an element
# not present in my_set
my_set.discard(2)
print(my_set)
# Output: {1, 3, 5}

# remove an element
# not present in my_set
# you will get an error.
# Output: KeyError
# my_set.remove(2)
