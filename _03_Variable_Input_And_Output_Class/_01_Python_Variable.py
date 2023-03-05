# Python Variables

"""
[01] Introduction of Python Variable:

> Python Variable is containers which store values.
>  Python is not “statically typed”. We do not need to declare variables before using them or declare their type.

> A variable is created the moment we first assign a value to it.
> A Python variable is a name given to a memory location.
> It is the basic unit of storage in a program.

> A variable is a reference to an object
"""

value = "Hello World!"
print(value)

"""
Notes:

- The value stored in a variable can be changed during program execution.
- A Python Variables is only a name given to a memory location, 
  all the operations done on the variable effects that memory location.
"""

"""
[02] Rules for creating variables in Python:

> A variable name must start with a letter or the underscore character.
> A variable name cannot start with a number.
> A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ ).
> Variable names are case-sensitive (name, Name and NAME are three different variables).
> The reserved words(keywords) cannot be used naming the variable.
"""

name = "Hasan Mahmud"
age = "28"

print(name)
print(age)

# [03] Declare the Variable

# declaring the variable
num = 10
# display
print(num)

# [04] Re-declare the Variable [We can re-declare the python variable once we have declared the variable already.]

num = 100
print(num)

# [05] Assigning a single value to multiple variables

num1 = num2 = num3 = 100
print(num1)
print(num2)
print(num3)

# [06] Assigning different values to multiple variables

name, age, country = "Hasan Mahmud", 28, "Bangladesh"

print(name)
print(age)
print(country)

# [07] Can we use the same name for different types?

value = 10
# If we use the same name, the variable starts referring to a new value and type.
value = "Python"

print(value)

# [08] Variable Type

"""
> Data types are the classification or categorization of data items.
> Since everything is an object in Python programming, 
  data types are actually classes and variables are instance (object) of these classes.

Following are the standard or built-in data type of Python:

1. Numeric
2. Sequence Type
3. Boolean
4. Set
5. Dictionary
"""

# [09] Object References

# Let, we assign a variable num to value 5, and
num = 5

# Another variable is num2 to the variable x.

num2 = num

# This situation, with multiple names referencing the same object, is called a *Shared Reference* in Python.

# [10] Tips for better Variable Names

"""
1. Must follow one case during the variable name declaration

> Camel Case - In the camel case, each word or abbreviation in the middle of begins with a capital letter. 
  There is no intervention of whitespace. For example - nameOfStudent, valueOfVaraible, etc.
> Pascal Case - It is the same as the Camel Case, but here the first word is also capital. For example - NameOfStudent, etc.
> Snake Case - In the snake case, Words are separated by the underscore. For example - name_of_student, etc.

2. Revealing Intent:  Variable names should express their purpose 

3. Search-ability:  Variable name should be easy to find in your codebase. 
"""
