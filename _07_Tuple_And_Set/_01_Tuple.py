## Python Tuples

"""
- Tuple is a collection of Python objects much like a list.
- The sequence of values stored in a tuple can be of any type,
  and they are indexed by integers.
- Values of a tuple are syntactically separated by ‘commas’.

- Tuple items are ordered, unchangeable, and allow duplicate values.
"""

## Creating a Tuple

# Creating an empty Tuple
Tuple1 = ()
print(Tuple1)  # ()

Tuple1 = tuple()
print(Tuple1) # ()

# Creating a Tuple with the use of string
Tuple1 = ('Python', 'Java')
print(Tuple1)  # ('Python', 'Java')

# Creating a Tuple with the use of list
list1 = [1, 2, 4, 5, 6]
print(tuple(list1))  # (1, 2, 4, 5, 6)

# Creating a Tuple with the use of built-in function
Tuple1 = tuple('Java')
print(Tuple1)  # ('J', 'a', 'v', 'a')

# Creating a Tuple with Mixed Datatypes.

# Creating a Tuple with Mixed Datatype
Tuple1 = (5, 'Welcome', 7.5, 'Java')
print(Tuple1)  # (5, 'Welcome', 7.5, 'Java')

## Accessing of Tuples

"""
- Tuples are immutable, and usually, they contain a sequence of heterogeneous elements 
  that are accessed via unpacking or indexing
- Lists are mutable, and their elements are usually homogeneous and are accessed by iterating over the list.
"""

Tuple = (1, 2, 3, 4, 5.5)
print(Tuple[0]) # 1
print(Tuple[-1]) # 5.5
print(Tuple[2:4]) # (3, 4) # The search will start at index 2 (included) and end at index 4 (not included).
print(Tuple[:4]) # (1, 2, 3, 4)
print(Tuple[2:]) # (3, 4, 5.5)
print(Tuple[-4:-1]) # (2, 3, 4)

print(1 in Tuple) # True

## Concatenation of Tuples

Tuple2 = (0, 1, 2, 3)
Tuple3 = ('Python', 'Java', 'C')

Tuple4 = Tuple2 + Tuple3

# Printing first Tuple
print(Tuple4) # (0, 1, 2, 3, 'Python', 'Java', 'C')

## Slicing of Tuple

Tuple5 = tuple('Python')
# Removing First element
print(Tuple5[1:]) # ('y', 't', 'h', 'o', 'n')
# Reversing the Tuple
print(Tuple5[::-1]) # ('n', 'o', 'h', 't', 'y', 'P')
# Printing elements of a Range
print(Tuple5[4:5]) # ('o',)

## Deleting a Tuple

"""
Tuples are immutable and hence they do not allow deletion of a part of it. 
The entire tuple gets deleted by the use of del() method. 
Note- Printing of Tuple after deletion results in an Error. 
"""
Tuple6 = (0, 1, 2, 3, 4)
del Tuple6

print(Tuple6) # name 'Tuple6' is not defined.

"""
Tuples VS Lists:
-------------------
In other words, a tuple is immutable whereas a list is mutable.
-------------------
- You can't add elements to a tuple. Tuples have no append or extend method.
- You can't remove elements from a tuple. Tuples have no remove or pop method.
- You can find elements in a tuple, since this doesn’t change the tuple.
- You can also use the in operator to check if an element exists in the tuple.
-------------------
Must it be mutable? Use a list. Must it not be mutable? Use a tuple.
Otherwise, it's a question of choice.
-------------------
I believe (and I am hardly well-versed in Python) that the main difference is 
that a tuple is immutable (it can't be changed in place after assignment) 
and a list is mutable (you can append, change, subtract, etc).

So, I tend to make my tuples things that shouldn't change after assignment and my lists things that can.
--------------------
"""






