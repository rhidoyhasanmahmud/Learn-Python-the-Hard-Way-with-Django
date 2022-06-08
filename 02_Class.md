## 🔧 Class - 02 Topics

| SL  | Topics                  | 
|-----|-------------------------|
| 01  | Python print() Function |
| 02  | Python Variables        |
| 02  | Python Data Types       |

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