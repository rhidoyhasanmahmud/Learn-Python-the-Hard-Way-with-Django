"""

- In Python, every object that is created is given a number that uniquely identifies it.
- It is guaranteed that no two objects will have the same identifier during any period in which their lifetimes overlap.
- The built-in Python function id() returns an object’s integer identifier.
- Using the id() function, you can verify that two variables indeed point to the same object.

- A variable is a reference to an object
"""

num1 = 10
num2 = 10
num3 = 20
num4 = 30

print(id(num1))  # 2418696585744
print(id(num2))  # 2418696585744
print(id(num3))  # 2418696586064
print(id(num4))  # 2418696586384

# Notice that id() value of ‘num1’ and ‘num2’ are same, they have the same integer value.
