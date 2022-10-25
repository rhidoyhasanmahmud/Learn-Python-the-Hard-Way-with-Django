"""
Generator-Function:

A generator-function is defined like a normal function, but whenever it needs to generate a value,
it does so with the yield keyword rather than return.

If the body of a def contains yield, the function automatically becomes a generator function.
"""


# A generator function that yields 1 for first time,
# 2 second time and 3 third time
def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3


# Driver code to check above generator function
for value in simpleGeneratorFun():
    print(value)

"""
1
2
3
"""

"""
Generator-Object : Generator functions return a generator object. Generator objects are used either by 
calling the next method on the generator object or using the generator object in a “for in” loop 
"""


# A Python program to demonstrate use of
# generator object with next()

# A generator function
def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3


# x is a generator object
x = simpleGeneratorFun()

# Iterating over the generator object using next
print(next(x))  # In Python 3, __next__()
print(next(x))
print(next(x))

"""
1
2
3
"""


# So a generator function returns an generator object that is iterable, i.e., can be used as an Iterators .

# A simple generator for Fibonacci Numbers
def fib(limit):
    # Initialize first two Fibonacci Numbers
    a, b = 0, 1

    # One by one yield next Fibonacci Number
    while a < limit:
        yield a
        a, b = b, a + b


# Create a generator object
x = fib(5)

# Iterating over the generator object using next
print(next(x))  # In Python 3, __next__()
print(next(x))
print(next(x))
print(next(x))
print(next(x))

# Iterating over the generator object using for
# in loop.
print("\nUsing for in loop")
for i in fib(5):
    print(i)

"""

0
1
1
2
3

Using for in loop
0
1
1
2
3

"""

"""
Yield vs Return in Python

Return. A function that returns a value is called once. The return statement returns a value and exits the function altogether.

Yield. A function that yields values, is called repeatedly. The yield statement pauses the execution of a function and 
returns a value. When called again, the function continues execution from the previous yield. A function that yields 
values is known as a generator.
"""


# Example

def square(numbers):
    result = []
    for n in numbers:
        result.append(n ** 2)
    return result


numbers = [1, 2, 3, 4, 5]
squared_numbers = square(numbers)
print(squared_numbers)  # [1, 4, 9, 16, 25]


# Example

def square(numbers):
    for n in numbers:
        yield n ** 2


numbers = [1, 2, 3, 4, 5]
squared_numbers = square(numbers)
print(squared_numbers)  # <generator object square at 0x7f685175b510>
print(next(squared_numbers))  # 1
print(next(squared_numbers))  # 4
print(next(squared_numbers))  # 9
print(next(squared_numbers))  # 16
print(next(squared_numbers))  # 25

"""
>> Why use Generator? 

1. Generator functions allow you to declare a function that behaves like an iterator.
2. They allow programmers to make an iterator in a fast, easy, and clean way.
3. Consider using Generator when dealing with a huge dataset
4. Consider using Generator in scenarios where we do NOT need to reiterate it more than once
5. Generators give us lazy evaluation
6. They are a great way to generate sequences in a memory-efficient manner
"""
