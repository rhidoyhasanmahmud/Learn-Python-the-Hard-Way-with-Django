# [01] What is == Operator?

# To compare objects based on their values, Python’s equality operators (==)

# [02] What is the ‘is’ Operator?

# Python identity operators (is, is not) are used to compare objects based on their identity.

# Equality operator
a = 10
b = 10

# Case 1:
# Return True because both a and b have the same value
print(a == b)  # True

# Case 2:
# Return True because both a and b is pointing to the same object
print(id(a))  # 2999413244432

print(id(b))  # 2999413244432

print(a is b)  # True

# Case 3:
# Here variable a is assigned to new variable c,
# which holds same object and same memory location
c = a
print(id(c))  # 2999413244432

print(a is c)  # True

'''
Summary: 

> The ‘is’ is known as the identity operator.
> The ‘==’ is known as the equality operator.

> When the variables on either side of an operator point at the exact same object, 
  the is operator’s evaluation is true. Otherwise, it will evaluate as False.
> When the variables on either side have the exact same value, 
  the == operator evaluation is true. Otherwise, it will evaluate as False.
'''
