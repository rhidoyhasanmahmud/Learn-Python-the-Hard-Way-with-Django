"""
In Python, an anonymous function means that a function is without a name.
As we already know that def keyword is used to define the normal functions
and the lambda keyword is used to create anonymous functions.

Python lambda Syntax:

lambda arguments : expression
"""

calc = lambda num: "Even number" if num % 2 == 0 else "Odd number"

print(calc(20))  # Even number

"""
Python lambda properties:
- This function can have any number of arguments but only one expression, which is evaluated and returned.
- One is free to use lambda functions wherever function objects are required.
- You need to keep in your knowledge that lambda functions are syntactically restricted to a single expression.
- It has various uses in particular fields of programming, besides other types of expressions in functions.
"""

# Example 1: Program to demonstrate return type of Python lambda keyword

string = 'Python'

# lambda returns a function object
print(lambda string: string)  # <function <lambda> at 0x7fd79817ade18>

"""
Explanation: In this above example, the lambda is not being called by the print function, 
but simply returning the function object and the memory location where it is stored. 
So, to make the print to print the string first, we need to call the lambda so that the string will get pass the print.
"""

# Example 2: Invoking lambda return value to perform various operations

"""
Here we have passed various types of arguments into the different lambda functions and printing the result generated 
from the lambda function calls.
"""

filter_nums = lambda s: ''.join([ch for ch in s if not ch.isdigit()])
print("filter_nums():", filter_nums("Python101"))

do_exclaim = lambda s: s + '!'
print("do_exclaim():", do_exclaim("I am tired"))

find_sum = lambda n: sum([int(x) for x in str(n)])
print("find_sum():", find_sum(101))

"""
Output:

filter_nums(): Python
do_exclaim(): I am tired!
find_sum(): 2
"""

# Example 3: Difference between lambda and normal function call

"""
- The lambda functions can be used without any declaration in the namespace. There is no return keyword defined 
explicitly because the lambda function does return an object by default.
- Lambda: Execution time of the program is fast for the same operation

"""


def cube(y):
    print(f"Finding cube of number:{y}")
    return y * y * y


lambda_cube = lambda num: num ** 3

# invoking simple function
print("invoking function defined with def keyword:")
print(cube(30))
# invoking lambda function
print("invoking lambda function:", lambda_cube(30))

"""
Output:
invoking function defined with def keyword:
Finding cube of number:30
27000
invoking lambda function: 27000
"""

# Example 4: The lambda function gets more helpful when used inside a function.

"""
We can use lambda function inside map(), filter(), sorted() and many other functions. 
Here, we have demonstrated how to use lambda function inside some of the most common Python functions.
"""

l = ["1", "2", "9", "0", "-1", "-2"]
# sort list[str] numerically using sorted()
# and custom sorting key using lambda
print("Sorted numerically:", sorted(l, key=lambda x: int(x)))

# filter positive even numbers
# using filter() and lambda function
print("Filtered positive even numbers:", list(filter(lambda x: not (int(x) % 2 == 0 and int(x) > 0), l)))

# added 10 to each item after type and
# casting to int, then convert items to string again
print("Operation on each item using lambda and map()", list(map(lambda x: str(int(x) + 10), l)))

"""
Sorted numerically: ['-2', '-1', '0', '1', '2', '9']
Filtered positive even numbers: ['1', '9', '0', '-1', '-2']
Operation on each item using lambda and map() ['11', '12', '19', '10', '9', '8']
"""

# 1). The map() function:

"""
The map() function is a higher-order function. 
As previously stated, this function accepts another function and a sequence of ‘iterables’ as parameters 
and provides output after applying the function to each iterable in the sequence. 

SYNTAX: map(function, iterables)
"""


# Define the transformation function
def cube(num):
    return num ** 3


# List of numbers to transform
num = [2, 3, 6, 9, 10]
# Call map function to apply cube on each number
cubed = map(cube, num)  # cubed = map(lambda n: n ** 3, num)
# Create a list containing the cubed values
print(list(cubed))  # [8, 27, 216, 729, 1000]

# 2). The filter() function:
"""
The filter() function is used to generate an output list of values that return true when the function is called. 

It has the following syntax:
SYNTAX: filter (function, iterables)
"""

# List of numbers
num = [12, 37, 34, 26, 9, 250, 451, 3, 10]

# Define lambda function to filter even numbers
even = list(filter(lambda x: (x % 2 == 0), num))

# Print the even numbers
print(even)  # [12, 34, 26, 250, 10]

# 3). The reduce() function:

"""
The reduce() function applies a provided function to ‘iterables’ and returns a single value, as the name implies.
SYNTAX: reduce(function, iterables)
"""
from functools import reduce


def add(x, y):
    return x + y


list = [2, 4, 7, 3]
print(reduce(add, list))
