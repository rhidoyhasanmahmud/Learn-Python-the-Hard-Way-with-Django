# Python Functions

"""
> Python Functions is a block of statements that return the specific task.

The idea is to put some commonly or repeatedly done tasks together and make a function
so that instead of writing the same code again and again for different inputs,
we can do the function calls to reuse code contained in it over and over again.
"""

## [01] Creating a Python Function

"""
> We can create a  Python function using the def keyword.
"""


# [02] A simple Python function <<<<
def fun():
    print("Welcome to Python World")


# [03] Calling a  Python Function <<<<

# A simple Python function
def printValue():
    print("Welcome to Python World")


# Driver code to call a function
printValue()  # Welcome to Python World


## [04] Defining and calling a function with parameters <<<<

# Example - 1

def add(num1: int, num2: int) -> int:
    """Add two numbers"""
    num3 = num1 + num2

    return num3


# Driver code
num1, num2 = 5, 15
ans = add(num1, num2)
print(f"The addition of {num1} and {num2} results {ans}.")  # The addition of 5 and 15 results 20.


# Example - 2

def is_prime(n):
    if n in [2, 3]:
        return True
    if (n == 1) or (n % 2 == 0):
        return False
    r = 3
    while r * r <= n:
        if n % r == 0:
            return False
        r += 2
    return True


print(is_prime(78), is_prime(79))  # False True


## [05] Arguments of a Python Function <<<<

# Ex. A simple Python function to check whether x is even or odd

def evenOdd(x):
    if x % 2 == 0:
        print("even")
    else:
        print("odd")


# Driver code to call the function
evenOdd(2)
evenOdd(3)


## [06] Types of Arguments

### 01. Default arguments

def myFun(x, y=50):
    print("x: ", x)
    print("y: ", y)


# Driver code (We call myFun() with only
# argument)
myFun(10)


### 02. Keyword arguments

# Python program to demonstrate Keyword Arguments
def student(firstname, lastname):
    print(firstname, lastname)


# Keyword arguments
student(firstname='Python', lastname='Java')
student(lastname='Java', firstname='Python')

### 03. Variable-length arguments

"""Variable length non-keywords argument"""


# Python program to illustrate
# [07] *args for variable number of arguments


def myFun(*argv):
    for arg in argv:
        print(arg)


myFun('Hello', 'Welcome', 'to', 'Python')

"""Variable length keyword arguments"""


# Python program to illustrate
# [08] *kwargs for variable number of keyword arguments


def myFun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))


# Driver code
myFun(first='Python', mid='for', last='Python')

## [09] Docstring

"""
The first string after the function is called the Document string or Docstring in short. 
This is used to describe the functionality of the function. 
The use of docstring in functions is optional but it is considered a good practice.
"""


# A simple Python function to check
# whether x is even or odd


def evenOdd(x):
    """Function to check if the number is even or odd"""

    if x % 2 == 0:
        print("even")
    else:
        print("odd")


# Driver code to call the function
print(evenOdd.__doc__)

## Return statement in Python function

"""
The function return statement is used to exit from a function and go back to the function caller 
and return the specified value or data item to the caller. 
"""


def square_value(num):
    """This function returns the square
    value of the entered number"""
    return num ** 2


print(square_value(2))
print(square_value(-4))


## Pass by Reference or pass by value


# Here x is a new reference to same list lst
def myFun(x):
    x[0] = 20


# Driver Code (Note that lst is modified
# after function call.
lst = [10, 11, 12, 13, 14, 15]
myFun(lst)
print(lst)
