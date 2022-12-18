"""
>> Comprehensions in Python

- We can create new sequences using a given python sequence. This is called comprehension.

- It basically a way of writing a concise code block to generate a sequence
  which can be a list, dictionary, set or a generator by using another sequence.

- It may involve multiple steps of conversion between different types of sequences.
"""

"""
>> List Comprehension

- we create a new list by manipulating the values of an existing list. 
"""

given_list = [x for x in range(5)]
print(given_list)  # [0, 1, 2, 3, 4]

new_list = [var + 3 for var in given_list]

print(new_list)  # [3, 4, 5, 6, 7]

lst_comprehension_2 = [num for num in lst if num % 2 == 1]
print(lst_comprehension_2)

"""
>> Dictionary Comprehensions
"""
given_list = [x for x in range(5)]
print(given_list) # [0, 1, 2, 3, 4]

new_dict = {var:var + 3 for var in given_list }

print(new_dict) # {0: 3, 1: 4, 2: 5, 3: 6, 4: 7}



"""
>> Set Comprehension
"""
given_set = {x for x in range(5)}
print(given_set) # {0, 1, 2, 3, 4}

new_set = {var+3 for var in given_set}

print(new_set) # {3, 4, 5, 6, 7}

# Tuple Comprehension

my_tuple = tuple(num for num in range(5))
my_tuple_2 = *(num for num in range(5)),

print(my_tuple)
print(my_tuple_2)

