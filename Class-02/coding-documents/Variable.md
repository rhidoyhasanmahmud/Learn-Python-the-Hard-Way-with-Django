# Declaring Variable and Assigning Values

```python
num1 = 100
```

```text
# The variable 'num1' refers to an integer object.
# Suppose we assign the integer value 100 to a new variable 'num2'.
```

```python
num1 = 100
num2 = num1
```

```text
# The variable 'num2' refers to the same object that 'num1' points to because Python does not create another object.
# Python manages memory efficiently if we assign the same variable to two different values.
```

```python
num3 = 10
num4 = 20
```

```text
# Now both variables will refer to the different objects.
```

# Object Identity

```text
# In Python, every created object identifies uniquely in Python.
# Python provides the guaranteed that no two objects will have the same identifier. 
# The built-in id() function, is used to identify the object identifier.
```

```python
num5 = 10
num6 = num5
print(id(num5))  # 2043972616720
print(id(num6))  # 2043972616720
```

# Multiple Assignment

```text
# Python allows us to assign a value to multiple variables in a single statement, which is also known as multiple assignments.
```

> 1. Assigning single value to multiple variables

```python
num1 = num2 = num3 = 100
print(num1)
print(num2)
print(num3)
```

> 2. Assigning multiple values to multiple variables:

```python
num1, num2, num3 = 10, 100, 1000
print(num1)
print(num2)
print(num3)
```

# Delete a variable

```text
# We can delete the variable using the del keyword.
```

```python
# Assigning a value to num
num = 100
print(num)
# deleting a variable.   
del num
print(num)  # NameError: name 'num' is not defined.
```

# Print Single and Multiple Variable

```python
# printing single value   
num = 100
print(num)  
```

```python
num1 = 5
num2 = 6

# printing multiple variables  
print(num1, num2)

# separate the variables by the comma  
print(1, 2, 3, 4, 5, 6, 7, 8)   
```


