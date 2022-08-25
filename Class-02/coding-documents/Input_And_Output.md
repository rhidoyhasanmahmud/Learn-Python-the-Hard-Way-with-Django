# Python get user input with a message

```python
# Taking input from the user
name = input("Enter your name: ")

# Output
print("Hello, " + name)
print(type(name))
```

# Integer input in Python

```python
# Taking input from the user as integer
num = int(input("Enter a number: "))

add = num + 1

# Output
print(add)
```

# Take Multiple Inputs in Python :

```python
a, b, c = map(int, input("Enter the Numbers : ").split())
print("The Numbers are : ", end=" ")
print(a, b, c)
```

# How to Display Output in Python

```text
Syntax: print(value(s), sep= ' ', end = '\n', file=file, flush=flush)

Parameters:

1. value(s) : Any value, and as many as you like. 
              Will be converted to string before printed.

2. sep='separator' : (Optional) Specify how to separate the objects, 
                     if there is more than one.Default :' '
                     
3. end='end': (Optional) Specify what to print at the end.Default : '\n'

4. file : (Optional) An object with a write method. Default :sys.stdout

5. flush : (Optional) A Boolean, specifying if the output is flushed (True) or buffered (False). Default: False

Returns: It returns output to the screen.
```

# Python Print Output

```python

# Python program to demonstrate
# print() method
print("GFG")

# code for disabling the softspace feature 
print('G', 'F', 'G')
```

# Formatting Output

```python
# Declaring a variable
name = "Hasan"

# Output
print(f'Hello {name}! How are you?')
```

## Using format()

```python
# Initializing variables
a = 20
b = 10

# addition
sum = a + b

# subtraction
sub = a - b

# Output
print('The value of a is {} and b is {}'.format(a, b))

print('{2} is the sum of {0} and {1}'.format(a, b, sum))
```

## Using % Operator

```text
# We can use ‘%’ operator. % values are replaced with zero or more value of elements.

%d – integer
%f – float
%s – string
%x – hexadecimal
%o – octal
```

```python
# Taking input from the user
num = int(input("Enter a value: "))
 
add = num + 5
 
# Output
print("The sum is %d" %add)
```