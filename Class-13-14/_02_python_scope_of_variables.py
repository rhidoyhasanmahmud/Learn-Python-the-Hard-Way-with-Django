"""
In Python, variables are the containers for storing data values. They are reference, or pointers, to an object in memory
which means that whenever a variable is assigned to an instance, it gets mapped to that instance.
"""
# Python program to demonstrate
# variable assignment

# An integer assignment
age = 45

# A floating point
salary = 1456.8

# A string
name = "John"

print(age)
print(salary)
print(name)

"""
Scope of variable
The location where we can find a variable and also access it if required is called the scope of a variable.
"""

# Global and local variables

"""
Global variables are the ones that are defined and declared outside any function and are not specified to any function. 
They can be used by any part of the program.
"""


# This function uses global variable s
def printMessage():
    print(message)


# Global scope
message = "I love Python"
printMessage()

"""
Now suppose a variable with the same name is defined inside the scope of function as well 
then it will print the value given inside the function only and not the global value.
"""

# Example - 01

# This function has a variable with
# name same as s.
def printMessage():
    message = "Me too."
    print(message)


# Global scope
message = "I love Python"
printMessage()
print(message)

# Example - 02

# This function modifies global variable 's'
def printMessage():
    global message
    print(message)
    message = "Look for eShikhon Python Section"
    print(message)


# Global Scope
message = "Python is great !"
printMessage()
print(message)