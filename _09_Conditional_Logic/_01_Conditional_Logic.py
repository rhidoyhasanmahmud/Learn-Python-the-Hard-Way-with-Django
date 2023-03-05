"""
- Decision-making is as important in any programming language as it is in life.

- Decision-making in a programming language is automated using conditional statements,
in which Python evaluates the code to see if it meets the specified conditions.

- The conditions are evaluated and processed as true or false.

> Python has six conditional statements that are used in decision-making:-

1. If the statement
2. If else statement
3. Nested if statement
4. If…Elif ladder
5. Short Hand if statement
6. Short Hand if-else statement
"""

## 01. If Statement

"""
if condition
 # Will executes this block if the condition is true
"""

# Example - 1
num = 5
if num > 0:
    print(num, "is a positive number.")  # 5 is a positive number.

# Example - 2

a = 25
b = 170
if b > a:
    print("b is greater than a")

## 02. If Else Statement
"""
if condition:
    # Will executes this block if the condition is true
else:
    # Will executes this block if the condition is false
"""

# Example – 1

num = 5
if num >= 0:
    print("Positive or Zero")
else:
    print("Negative number")
# output : Positive or Zero

## 03. If…Elif..else Statement

"""
if condition :
    # Will executes this block if the condition is true
elif condition :
    # Will executes this block if the condition is true
else: 
    # Will executes this block if the conditions is false
"""

# Example – 1

num = 7
if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")
# output:  Positive number

## 04. Nested IF Statement

"""
if condition1:
  # Will executes this block if the condition is true
if condition 2:
  # Will executes this block if the condition is true
"""

# Example-1

num = 8
if num >= 0:
    if num == 0:
        print("zero")
    else:
        print("Positive number")
else:
    print("Negative number")
# output: Positive number

## 05. Short Hand if statement

"""
if condition: statement
"""
i = 15
# One line if statement
if i > 11: print("i is greater than 11")
# The output of the program : "i is greater than 11."

## 06 Short Hand if-else statement

a = 3
b = 5
print("A") if a > b else print("B")

# output: B


### Switch Case in Python :

argument = 0

match argument:
    case 0:
        print("zero")
    case 1:
        print("one")
    case 2:
        print("two")
    case default:
        print("something")

# output: zero
