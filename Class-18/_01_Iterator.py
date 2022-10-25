"""
>> Iterators in Python

- Iterator in Python is an object that is used to iterate over iterable objects like lists, tuples, dicts, and sets.

- The iterator object is initialized using the iter() method. It uses the next() method for iteration.

------------
__iter__(): The iter() method is called for the initialization of an iterator. This returns an iterator object.

__next__(): The next method returns the next value for the iterable.
------------
When we use a for loop to traverse any iterable object, internally it uses the iter() method to get an iterator object,
which further uses the next() method to iterate over.
This method raises a StopIteration to signal the end of the iteration.
------------
The __next__() method will raise a StopIteration exception if there are no further elements available.
"""

# Python iter()

string = "eShikhon"
ch_iterator = iter(string)

print(next(ch_iterator))  # e
print(next(ch_iterator))  # S
print(next(ch_iterator))  # h

# Example 1: Iterating over built-in iterables using iter() method

# Iterating over a list
print("List Iteration")
lst = ["Python", "Java", "JavaScript"]
for value in lst:
    print(value)

"""
List Iteration
Python
Java
JavaScript
"""

# Iterating over a tuple (immutable)
print("\nTuple Iteration")
tpl = ("Python", "Java", "JavaScript")
for i in tpl:
    print(i)

"""
Tuple Iteration
Python
Java
JavaScript
"""

# Iterating over a String
print("\nString Iteration")
s = "Python"
for i in s:
    print(i)

"""
String Iteration
P
y
t
h
o
n
"""

# Iterating over dictionary
print("\nDictionary Iteration")
dct = dict()
dct['name'] = "Hasan Mahmud"
dct['age'] = "34"

for i in dct:
    print("%s  %s" % (i, dct[i]))

"""
Dictionary Iteration
name  Hasan Mahmud
age  34
"""

# Iterable vs Iterator

"""
>>
The main difference between them is, iterable cannot save the state of the iteration, 
but whereas in iterators the state of the current iteration gets saved.
<<
Iterable is an object, that one can iterate over. It generates an Iterator when passed to iter() method.
An iterator is an object, which is used to iterate over an iterable object using the __next__() method.
Iterators have the __next__() method, which returns the next item of the object.
>>
Every iterator is also an iterable, but not every iterable is an iterator in Python.
<< 
"""

# Getting StopIteration Error while using iterator

iterable = (1, 2, 3, 4)
iterator_obj = iter(iterable)

print("Iterable loop 1:")
# iterating on iterable
for item in iterable:
    print(item, end=",")

print("\nIterable Loop 2:")
for item in iterable:
    print(item, end=",")

print("\nIterating on an iterator:")
# iterating on an iterator object multiple times
for item in iterator_obj:
    print(item, end=",")

print("\nIterator: Outside loop")
# this line will raise StopIteration Exception
# since all items are iterated in the previous for-loop
print(next(iterator_obj))

"""
Iterable loop 1:
1,2,3,4,
Iterable Loop 2:
1,2,3,4,
Iterating on an iterator:
1,2,3,4,
Iterator: Outside loop


Traceback (most recent call last):
  File "H:\Python_Batch_3\Class-18\test.py", line 125, in <module>
    print(next(iterator_obj))
StopIteration
"""

"""
In the above code, we are trying to get the next element from the iterator after the completion of the for-loop. 
Since the iterator is already exhausted, it raises a StopIteration Exception. 
Whereas, using an iterable, we can iterate on multiple times using for loop or can get items using indexing.
"""
