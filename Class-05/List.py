"""
>> Python List

- A list in Python is used to store the sequence of various types of data.
- Python lists are mutable type its mean we can modify its element after it created.
- Python Lists are just like dynamically sized arrays.
- List is a sequence data type which is used to store the collection of data.

- The items in the list are separated with the comma (,) and enclosed with the square brackets [].

>> Characteristics of Lists

- The lists are ordered.
- The element of the list can access by index.
- The lists are the mutable type.
- A list can store the number of various elements.
"""

## Creating a List in Python

"""
- Lists in Python can be created by just placing the sequence inside the square brackets[]. 
"""

# Creating a empty List
List = [] # Blank List
print(List) # []

# Creating a List of numbers
List = [10, 20, 14]
print(List) # [10, 20, 14]

# Creating a List with the use of Numbers (Having duplicate values)
List = [1, 2, 4, 4, 3, 3, 3, 6, 5]
print(List) # [1, 2, 4, 4, 3, 3, 3, 6, 5]

# Creating a List with mixed type of values (Having numbers and strings)
List = [1, 2, 'Python', 4, 'Java', 6.5, 'C++']
print(List) # [1, 2, 'Python', 4, 'Java', 6.5, 'C++']

## Accessing elements from the List

"""
- In order to access the list items refer to the index number.
- Use the index operator [ ] to access an item in a list. 
- The index must be an integer.
- Nested lists are accessed using nested indexing.
"""

# Creating a List with the use of multiple values
List = ["Python", "Java", "C++"]

print(List[0]) # Python
print(List[2]) # C++

# Creating a Multi-Dimensional List (By Nesting a list inside a List)
List = [['Java', 'Python'], ['PHP']]
print(List[0][1]) # Python
print(List[1][0]) # PHP

# Negative indexing
List = [1, 2, 'Python', 4, 'Java', 6, 'PHP']

# print the last element of list
print(List[-1]) # PHP

# print the third last element of list
print(List[-3]) # Java

## Getting the size of Python list

"""
- Python len() is used to get the length of the list.
"""

# Creating a List
List1 = []
print(len(List1)) # 0

# Creating a List of numbers
List2 = [10, 20, 14]
print(len(List2)) # 3

## Taking Input of a Python List

# Python program to take space separated input as a string
# Split and store it to a list and print the string list

# input the list as string
string = input("Enter elements (Space-Separated): ") # Enter elements: Python Java PHP

# split the strings and store it to a list
lst = string.split()
print('The list is:', lst)   # The list is: ['Python', 'Java', 'PHP']

## Adding Elements to a Python List

"""
> Using append() method
- Elements can be added to the List by using the built-in append() function.
- Only one element at a time can be added to the list by using the append() method
- append() method only works for the addition of elements at the end of the List
"""
# Creating a List
List = []

List.append(1)
List.append(2)
List.append(4)

print(List) # [1, 2, 4]

"""
> Using insert() methodUsing insert() method
- Elements at the desired position, insert() method is used.
- Unlike append() which takes only one argument, the insert() method requires two arguments(position, value).
"""
# Creating a List
List = [1,2,3,4]
print(List) # [1, 2, 3, 4]

List.insert(3, 12)
List.insert(0, 'Python')
print(List) # ['Python', 1, 2, 3, 12, 4]

"""
> Using extend() method
- extend(), method is used to add multiple elements at the same time at the end of the list.
- append() and extend() methods can only add elements at the end.
"""
List = [1, 2, 3, 4]
print(List) # [1, 2, 3, 4]

List.extend([8, 'Python', 'Java'])
print(List) # [1, 2, 3, 4, 8, 'Python', 'Java']

## Reversing a List

"""
- A list can be reversed by using the reverse() method in Python.
"""

mylist = [1, 2, 3, 4, 5, 'Java', 'Python']
mylist.reverse()
print(mylist) # ['Python', 'Java', 5, 4, 3, 2, 1]

## Removing Elements from the List

"""
> Using remove() method
- Elements can be removed from the List by using the built-in remove() function 
  but an Error arises if the element doesn’t exist in the list. 
- remove() method only removes one element at a time. 
- Remove method in List will only remove the first occurrence of the searched element.
"""

List = [1, 2, 3, 4, 5, 6,7, 8, 9, 10, 11, 12]
print(List) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

List.remove(5)
List.remove(6)
print(List) # [1, 2, 3, 4, 7, 8, 9, 10, 11, 12]

"""
> Using pop() method
- pop() function can also be used to remove and return an element from the list. 
- By default it removes only the last element of the list
- For specific position of the List, the index of the element is passed as an argument to the pop() method.
"""

List = [1, 2, 3, 4, 5]
List.pop()
print(List) # [1, 2, 3, 4]

List.pop(2)
print(List) # [1, 2, 4]

## Slicing of a List

"""
- We can get substrings and sublists using a slice.

- To print elements from beginning to a range use: [: Index]
- To print elements from end-use: [:-Index]
- To print elements from a specific Index till the end use: [Index:]
- To print the whole list in reverse order, use: [::-1]
"""
List = ['A', 'B', 'C', 'D', 'E', 'F','G', 'H', 'I', 'J', 'K', 'L', 'M']
print(List)
# ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']

Sliced_List = List[3:8]
print(Sliced_List) # ['D', 'E', 'F', 'G', 'H']
Sliced_List = List[5:]
print(Sliced_List) # ['F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']
Sliced_List = List[:]
print(Sliced_List) # ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']

# Negative index List slicing

List = ['A', 'B', 'C', 'D', 'E', 'F','G', 'H', 'I', 'J', 'K', 'L', 'M']
Sliced_List = List[:-6]
print(Sliced_List) # ['A', 'B', 'C', 'D', 'E', 'F', 'G']
Sliced_List = List[-6:-1]
print(Sliced_List) # ['H', 'I', 'J', 'K', 'L']
Sliced_List = List[::-1]
print(Sliced_List) # ['M', 'L', 'K', 'J', 'I', 'H', 'G', 'F', 'E', 'D', 'C', 'B', 'A']

"""
>> List Methods

Append()	Add an element to the end of the list
Extend()	Add all elements of a list to another list
Insert()	Insert an item at the defined index
Remove()	Removes an item from the list
Clear()	    Removes all items from the list
Index()	    Returns the index of the first matched item
Count()	    Returns the count of the number of items passed as an argument
Sort()	    Sort items in a list in ascending order
Reverse()	Reverse the order of items in the list
copy()	    Returns a copy of the list
any()	    return true if any element of the list is true. if the list is empty, return false
sum()	    Sums up the numbers in the list
max()	    return maximum element of a given list
min()	    return minimum element of a given list
all()	    Returns true if all element is true or if the list is empty
any()	    return true if any element of the list is true. if the list is empty, return false
len()	    Returns length of the list or size of the list
"""


