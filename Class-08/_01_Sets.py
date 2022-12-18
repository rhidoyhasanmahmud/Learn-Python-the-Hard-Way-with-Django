## Python Set Operations

### Set Union

# Set union method
# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# use | operator
print(A | B)
# Output: {1, 2, 3, 4, 5, 6, 7, 8}

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
# use union function
print(A.union(B))
# Output: {1, 2, 3, 4, 5, 6, 7, 8}

# use union function on B
print(B.union(A))
# Output: {1, 2, 3, 4, 5, 6, 7, 8}


### Set Intersection

# Intersection of sets
# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# use & operator
print(A & B)
# Output: {4, 5}

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
# use intersection function on A
print(A.intersection(B))
# {4, 5}

# use intersection function on B
print(B.intersection(A))
# {4, 5}

### Set Difference

# Difference of two sets
# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# use - operator on A
print(A - B)
# Output: {1, 2, 3}

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
# use difference function on A
print(A.difference(B))
# Output: {1, 2, 3}

# use - operator on B
print(B - A)
# Output: {8, 6, 7}

# use difference function on B
print(B.difference(A))
# Output: {8, 6, 7}

## Set Symmetric Difference

# Symmetric difference of two sets
# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# use ^ operator
# Output: {1, 2, 3, 6, 7, 8}
print(A ^ B)

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
# use symmetric_difference function on A
print(A.symmetric_difference(B))
# Output: {1, 2, 3, 6, 7, 8}

# use symmetric_difference function on B
print(B.symmetric_difference(A))
# Output: {1, 2, 3, 6, 7, 8}

"""
add()                           Adds an element to the set
clear()	                        Removes all elements from the set
copy()	                        Returns a copy of the set
difference()	                Returns the difference of two or more sets as a new set
difference_update()	            Removes all elements of another set from this set
discard()	                    Removes an element from the set if it is a member. (Do nothing if the element is not in set)
intersection()	                Returns the intersection of two sets as a new set
intersection_update()	        Updates the set with the intersection of itself and another
isdisjoint()	                Returns True if two sets have a null intersection
issubset()	                    Returns True if another set contains this set
issuperset()	                Returns True if this set contains another set
pop()	                        Removes and returns an arbitrary set element. Raises KeyError if the set is empty
remove()	                    Removes an element from the set. If the element is not a member, raises a KeyError
symmetric_difference()	        Returns the symmetric difference of two sets as a new set
symmetric_difference_update()	Updates a set with the symmetric difference of itself and another
union()	                        Returns the union of sets in a new set
update()	                    Updates the set with the union of itself and others
"""

# in keyword in a set
# initialize my_set
my_set = set("apple")

# check if 'a' is present
# Output: True
print('a' in my_set)

# check if 'p' is present
# Output: False
print('p' not in my_set)

## Python Frozenset

"""
- Frozenset is a new class that has the characteristics of a set, but its elements cannot be changed once assigned. 
  While tuples are immutable lists, frozensets are immutable sets.

- Sets being mutable are unhashable, so they can't be used as dictionary keys. On the other hand, 
  frozensets are hashable and can be used as keys to a dictionary.

- Frozensets can be created using the frozenset() function.

- This data type supports methods like copy(), difference(), intersection(), isdisjoint(), issubset(), issuperset(), 
  symmetric_difference() and union(). Being immutable, it does not have methods that add or remove elements.
"""

# Frozensets
# initialize A and B
A = frozenset([1, 2, 3, 4])
B = frozenset([3, 4, 5, 6])

print(A.isdisjoint(B))
# False
print(A.difference(B))
# frozenset({1, 2})
print(A | B)
# frozenset({1, 2, 3, 4, 5, 6})
print(A.add(3))
# AttributeError: 'frozenset' object has no attribute 'add'
