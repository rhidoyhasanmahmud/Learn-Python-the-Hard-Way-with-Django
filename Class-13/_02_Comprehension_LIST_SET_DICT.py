"""
- Comprehensions in Python provide us with a short and concise way to construct new sequences
(such as lists, set, dictionary etc.) using sequences which have been already defined.

Python supports the following 4 types of comprehensions:

1. List Comprehensions
2. Dictionary Comprehensions
3. Set Comprehensions
4. Generator Comprehensions
"""
# List Comprehensions:

"""
List Comprehensions provide an elegant way to create new lists. 

The following is the basic structure of a list comprehension:
output_list = [output_exp for var in input_list if (var satisfies this condition)]
"""

# Example #1: Suppose we want to create an output list which contains only the even numbers which are present
# in the input list. Let’s see how to do this using for loops and list comprehension
# and decide which method suits better.

# Constructing output list WITHOUT
# Using List comprehensions
input_list = [1, 2, 3, 4, 4, 5, 6, 7, 7]

output_list = []

# Using loop for constructing output list
for var in input_list:
    if var % 2 == 0:
        output_list.append(var)

print("Output List using for loop:", output_list)  # Output List using for loop: [2, 4, 4, 6]

# Using List comprehensions
# for constructing output list

input_list = [1, 2, 3, 4, 4, 5, 6, 7, 7]

list_using_comp = [var for var in input_list if var % 2 == 0]

print("Output List using list comprehensions:", list_using_comp)  # Output List using list comprehensions: [2, 4, 4, 6]

# Example #2: Suppose we want to create an output list which contains squares of all the numbers from 1 to 9.
# Let’s see how to do this using for loops and list comprehension.

# Constructing output list using for loop
output_list = []
for var in range(1, 10):
    output_list.append(var ** 2)

print("Output List using for loop:", output_list)  # Output List using for loop: [1, 4, 9, 16, 25, 36, 49, 64, 81]

# Constructing output list
# using list comprehension
list_using_comp = [var ** 2 for var in range(1, 10)]

print("Output List using list comprehension:", list_using_comp)
# Output List using list comprehension: [1, 4, 9, 16, 25, 36, 49, 64, 81]

# Dictionary Comprehensions:

"""
Extending the idea of list comprehensions, we can also create a dictionary using dictionary comprehensions. 

The basic structure of a dictionary comprehension looks like below.
output_dict = {key:value for (key, value) in iterable if (key, value satisfy this condition)}
"""

# Example #1: Suppose we want to create an output dictionary which contains only the odd numbers that are present
# in the input list as keys and their cubes as values. Let’s see how to do this using for loops
# and dictionary comprehension.

input_list = [1, 2, 3, 4, 5, 6, 7]

output_dict = {}

# Using loop for constructing output dictionary
for var in input_list:
    if var % 2 != 0:
        output_dict[var] = var ** 3

print("Output Dictionary using for loop:", output_dict)
# Output Dictionary using for loop: {1: 1, 3: 27, 5: 125, 7: 343}

# Using Dictionary comprehensions
# for constructing output dictionary

input_list = [1, 2, 3, 4, 5, 6, 7]

dict_using_comp = {var: var ** 3 for var in input_list if var % 2 != 0}

print("Output Dictionary using dictionary comprehensions:", dict_using_comp)
# Output Dictionary using dictionary comprehensions: {1: 1, 3: 27, 5: 125, 7: 343}

# Example #2: Given two lists containing the names of states and their corresponding capitals, construct a dictionary
# which maps the states with their respective capitals. Let’s see how to do this using for loops
# and dictionary comprehension.

state = ['Gujarat', 'Maharashtra', 'Rajasthan']
capital = ['Gandhinagar', 'Mumbai', 'Jaipur']

output_dict = {}

# Using loop for constructing output dictionary
for (key, value) in zip(state, capital):
    output_dict[key] = value

print("Output Dictionary using for loop:", output_dict)
"""
Output Dictionary using for loop: {'Gujarat': 'Gandhinagar',
                                   'Maharashtra': 'Mumbai', 
                                   'Rajasthan': 'Jaipur'}
"""

# Using Dictionary comprehensions
# for constructing output dictionary

state = ['Gujarat', 'Maharashtra', 'Rajasthan']
capital = ['Gandhinagar', 'Mumbai', 'Jaipur']

dict_using_comp = {key: value for (key, value) in zip(state, capital)}

print("Output Dictionary using dictionary comprehensions:", dict_using_comp)

"""
Output Dictionary using dictionary comprehensions: {'Rajasthan': 'Jaipur',
                                                    'Maharashtra': 'Mumbai',
                                                    'Gujarat': 'Gandhinagar'}
"""

# Set Comprehensions:

"""
Set comprehensions are pretty similar to list comprehensions. 
The only difference between them is that set comprehensions use curly brackets { }.
"""

# Example #1 : Suppose we want to create an output set which contains only the even numbers
# that are present in the input list.
# Note that set will discard all the duplicate values. Let’s see how we can do this using for loops
# and set comprehension.

input_list = [1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7]

output_set = set()

# Using loop for constructing output set
for var in input_list:
    if var % 2 == 0:
        output_set.add(var)

print("Output Set using for loop:", output_set)  # Output Set using for loop: {2, 4, 6}

# Using Set comprehensions
# for constructing output set

input_list = [1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7]

set_using_comp = {var for var in input_list if var % 2 == 0}

print("Output Set using set comprehensions:", set_using_comp)  # Output Set using set comprehensions: {2, 4, 6}

# Generator Comprehensions:

"""
- Generator Comprehensions are very similar to list comprehensions. 
- One difference between them is that generator comprehensions use circular brackets 
    whereas list comprehensions use square brackets.
- The major difference between them is that generators don’t allocate memory for the whole list. 
- Instead, they generate each value one by one which is why they are memory efficient.
"""

input_list = [1, 2, 3, 4, 4, 5, 6, 7, 7]

output_gen = (var for var in input_list if var % 2 == 0)

print("Output values using generator comprehensions:", end=' ')

for var in output_gen:
    print(var, end=' ')

# Output values using generator comprehensions: 2 4 4 6
