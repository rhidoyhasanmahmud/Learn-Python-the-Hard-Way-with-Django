## 🔧 Class - 02 Topics

| SL  | Topics                                               | 
|-----|------------------------------------------------------|
| 01  | Python print() Function                              |
| 02  | Python Variables                                     |
| 02  | Python Data Types |

## 📤 Python print() Function

⚙ The print() function displays the given object to the standard output device (screen) or to the text stream file.

⚙ The syntax of print() function is given below.

```python
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
```

Let's explain its parameters one by one.

⚙ objects - An object is nothing but a statement that to be printed. The * sign represents that there can be multiple
statements.

⚙ sep - The sep parameter separates the print values. Default values is ' '.

⚙ end - The end is printed at last in the statement.

⚙ file - It must be an object with a write(string) method.

⚙ flush - The stream or file is forcibly flushed if it is true. By default, its value is false.

> Example - 1: Return a value

```python
print("Welcome to Python.")

a = 10
# Two objects are passed in print() function  
print("a =", a)

b = a
# Three objects are passed in print function  
print('a =', a, '= b')

"""
Welcome to Python.
a = 10
a = 10 = b
"""
```

> Example - 2: Using sep and end argument

```python
a = 10
print("a =", a, sep='dddd', end='\n\n')
print("a =", a, sep='0', end='$$$$$')

"""
a =dddd10

a =010$$$$$
"""
```

> Example - 3: Taking Input to the User

Python provides the input() function which is used to take input from the user. Let's understand the following example.

```python
name = input("Enter a name of student:")
print("The student name is: ", name)

"""
Enter a name of student: Hasan Mahmud
The student name is: Hasan Mahmud
"""
```

> Example - 4:

If we want to take input as an integer number, we need to typecast the input() function into an integer.

```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(a + b)

"""
Enter first number: 50
Enter second number: 100
150
"""
```

## 📤 Python Variables

⚙ Variable is a name that is used to refer to memory location.

⚙ Python variable is also known as an identifier and used to hold value.

⚙ In Python, we don't need to specify the type of variable because Python is a infer language and smart enough to get
variable type.

> Identifier Naming

**⚙** The first character of the variable must be an alphabet or underscore ( _ ).

⚙ All the characters except the first character may be an alphabet of lower-case(a-z), upper-case (A-Z), underscore, or
digit (0-9).

⚙ Identifier name must not contain any white-space, or special character (!, @, #, %, ^, &, *).

⚙ Identifier name must not be similar to any keyword defined in the language.

⚙ Identifier names are case sensitive; for example, myname, and MyName is not the same.

⚙ Examples of valid identifiers: a123, _n, n_9, etc.

⚙ Examples of invalid identifiers: 1a, n%4, n 9, etc.

> Declaring Variable and Assigning Values

⚙ Python does not bind us to declare a variable before using it in the application. It allows us to create a variable at
the required time.

⚙ We don't need to declare explicitly variable in Python. When we assign any value to the variable, that variable is
declared automatically.

⚙ The equal (=) operator is used to assign value to a variable.

Consider the following example.

```python
print("Python")  # Python

type("Python")  # <class 'str'>
```

## 📤 Data type

Variables can hold values, and every value has a data-type. Python is a dynamically typed language; hence we do not need
to define the type of the variable while declaring it. The interpreter implicitly binds the value with its type.

```python
num = 5  
```

The variable **num** holds integer value five and we did not define its type. Python interpreter will automatically
interpret
variables **num** as an integer type.

Python enables us to check the type of the variable used in the program. Python provides us the **type()** function,
which
returns the type of the variable passed.

```python
num = 10
string_value = "Hello Python"
dicimalNum = 10.5
print(type(num))
print(type(string_value))
print(type(dicimalNum))

"""
<type 'int'>
<type 'str'>
<type 'float'>
"""
```

> Standard data types

A variable can hold different types of values.

Python provides various standard data types that define the storage method on each of them. The data types defined in
Python are given below.

1. Numbers [Integer, Complex Number, Float]
2. Sequence Type [Strings, List, Tuple]
3. Boolean
4. Set
5. Dictionary

> Numbers

Number stores numeric values. The integer, float, and complex values belong to a Python Numbers data-type. Python
provides the type() function to know the data-type of the variable. Similarly, the isinstance() function is used to
check an object belongs to a particular class.

```python
num = 5
print("The type of num", type(num))

floatNumber = 40.5
print("The type of floatNumber", type(floatNumber))

complexNumber = 1 + 3j
print("The type of complexNumber", type(complexNumber))
print(" complexNumber is a complex number", isinstance(1 + 3j, complex))

"""
The type of num <class 'int'>
The type of floatNumber <class 'float'>
The type of complexNumber <class 'complex'>
complexNumber is complex number: True
"""
```

Python supports three types of numeric data.

1. **Int** - Integer value can be any length such as integers 10, 2, 29, -20, -150 etc. Python has no restriction on the
   length of an integer. Its value belongs to int
2. **Float** - Float is used to store floating-point numbers like 1.9, 9.902, 15.2, etc. It is accurate upto 15 decimal
   points.
3. **Complex** - A complex number contains an ordered pair, i.e., x + iy where x and y denote the real and imaginary
   parts, respectively. The complex numbers like 2.14j, 2.0 + 2.3j, etc.

> Sequence Type

1. String

The string can be defined as the sequence of characters represented in the quotation marks. In Python, we can use
single, double, or triple quotes to define a string.

String handling in Python is a straightforward task since Python provides built-in functions and operators to perform
operations in the string.

```python
str = "string using double quotes"
print(str)
s = '''''A multiline 
string'''
print(s)

"""
string using double quotes
A multiline
string
"""
```

2. List [Discuss it later]
3. Tuple [Discuss it later]
4. Dictionary [Discuss it later]
5. Boolean

Boolean type provides two built-in values, True and False. These values are used to determine the given statement true
or false. It denotes by the class bool.

```python
print(type(True))
print(type(False))
print(false)
"""
<class 'bool'>
<class 'bool'>
NameError: name 'false' is not defined
"""
```

6. Set [Discuss it later]

> Assignment List

1. https://www.beecrowd.com.br/judge/en/problems/view/1000
2. https://www.beecrowd.com.br/judge/en/problems/view/1001

> Reference:

1. https://www.w3schools.com/python/
2. https://docs.python.org/3/tutorial/
3. https://www.tutorialspoint.com/python/index.htm
4. https://www.pythontutorial.net/
5. https://www.javatpoint.com/
6. https://www.programiz.com/python-programming