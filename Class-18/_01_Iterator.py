"""
>> What is an Iterator?

- An iterator is an object that is used to iterate or loop through the elements or items in the
  collections such as List, Set, etc.

- Iterator: the name came from iterating which is a technical term for looping the elements.

>> What is an Iterator in Python?

- An iterator is an object which is meant for the purpose in Python,
  is nothing but looping through iterable objects like lists, tuples, dicts, and sets.

>> Instantiating the Iterator in Python

The iterator consists of two methods:
1. iter() and
2. next().

Iter() method is used to initialize the iterator object so that the instance of this object can be used for iterating.

Syntax is:

myiterator = iter()

The next() method is used to iterate over the iterable objects. The next() method returns the next value in the iterable object.

Syntax is

item = next(myiterator)
"""

"""
Iterator vs Iterable

In Python, the List, Tuple, Set, and Dict are all iterable objects. These iterable objects have an iter() method 
which is used to get an iterator. It also considered the string object an iterable object in Python.
"""
tupleObj = ("Red", "Orange")

myiterator = iter(tupleObj)

print(next(myiterator))  # Red


