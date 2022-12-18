# A class is a user-defined blueprint or prototype from which objects are created.
# Classes provide a means of bundling data and functionality together.
# Creating a new class creates a new type of object, allowing new instances of that type to be made.

"""
>> Syntax: Class Definition

class ClassName:
    # Statement

>> Syntax: Object Definition

obj = ClassName()
print(obj.atrr)
"""

"""
Class creates a user-defined data structure, which holds its own data members and member functions, 
which can be accessed and used by creating an instance of that class. 
A class is like a blueprint for an object.

Some points on Python class:  

1. Classes are created by keyword class.
2. Attributes are the variables that belong to a class.
3. Attributes are always public and can be accessed using the dot (.) operator. Eg.: Myclass.Myattribute
"""


class Cat:
    pass


# In the above example,
# the class keyword indicates that you are creating a class followed by the name of the class (Cat in this case).

## >> Class Objects

"""
An Object is an instance of a Class. 
A class is like a blueprint while an instance is a copy of the class with actual values.

An object consists of : 

> State: It is represented by the attributes of an object. It also reflects the properties of an object.
> Behaviour: It is represented by the methods of an object. It also reflects the response of an object to other objects.
> Identity: It gives a unique name to an object and enables one object to interact with other objects.

Link: https://media.geeksforgeeks.org/wp-content/uploads/Blank-Diagram-Page-1-5.png
"""

## >> Declaring Objects (Also called instantiating a class)

"""
When an object of a class is created, the class is said to be instantiated. 
All the instances share the attributes and the behavior of the class. 
But the values of those attributes, i.e. the state are unique for each object. 
A single class may have any number of instances.

Link: https://media.geeksforgeeks.org/wp-content/uploads/Blank-Diagram-Page-1-3.png
"""


class Dog:
    # A simple class
    # attribute
    attr1 = "mammal"
    attr2 = "dog"

    # A sample method
    def fun(self):
        print("I'm a", self.attr1)
        print("I'm a", self.attr2)


# Driver code
# Object instantiation
roger = Dog()

# Accessing class attributes
# and method through objects
print(roger.attr1)
roger.fun()

"""
Output:

mammal
I'm a mammal
I'm a dog
"""

# The self and __init__ method

"""
- self is used to refer to the specific object that is calling that function
- The __init__ function is a constructor function meaning that it constructs objects in a class.
"""


# Sample class with init method
class Person:

    # init method or constructor
    def __init__(self, name):
        self.name = name

    # Sample Method
    def say_hi(self):
        print('Hello, my name is', self.name)


p = Person('Hasan')
p.say_hi()


# Class and Instance Variables

# Python3 program to show that the variables with a value
# assigned in the class declaration, are class variables and
# variables inside methods and constructors are instance
# variables.

# Class for Dog


class Dog:
    # Class Variable
    animal = 'dog'

    # The init method or constructor
    def __init__(self, breed, color):
        # Instance Variable
        self.breed = breed
        self.color = color


# Objects of Dog class
Rodger = Dog("Pug", "brown")
Buzo = Dog("Bulldog", "black")

print('Rodger details:')
print('Rodger is a', Rodger.animal)
print('Breed: ', Rodger.breed)
print('Color: ', Rodger.color)

print('\nBuzo details:')
print('Buzo is a', Buzo.animal)
print('Breed: ', Buzo.breed)
print('Color: ', Buzo.color)

# Class variables can be accessed using class
# name also
print("\nAccessing class variable using class name")
print(Dog.animal)

"""
Output
Rodger details:
Rodger is a dog
Breed:  Pug
Color:  brown

Buzo details:
Buzo is a dog
Breed:  Bulldog
Color:  black

Accessing class variable using class name
dog
"""


# Defining instance variables using the normal method.

# Python3 program to show that we can create
# instance variables inside methods

# Class for Dog


class Dog:
    # Class Variable
    animal = 'dog'

    # The init method or constructor
    def __init__(self, breed):
        # Instance Variable
        self.breed = breed

    # Adds an instance variable
    def setColor(self, color):
        self.color = color

    # Retrieves instance variable
    def getColor(self):
        return self.color


# Driver Code
Rodger = Dog("pug")
Rodger.setColor("brown")
print(Rodger.getColor())

"""
Output:

brown
"""

# Constructors in Python

"""
Constructors are generally used for instantiating an object. 
The task of constructors is to initialize(assign values) to the data members of the class 
when an object of the class is created. 

In Python the __init__() method is called the constructor and is always called when an object is created.

Syntax of constructor declaration : 

def __init__(self):
    # body of the constructor

Types of constructors : 

> Default constructor: The default constructor is a simple constructor which doesn’t accept any arguments. 
  Its definition has only one argument which is a reference to the instance being constructed.
> Parameterized constructor: constructor with parameters is known as parameterized constructor. 
The parameterized constructor takes its first argument as a reference to the instance being constructed known as self 
and the rest of the arguments are provided by the programmer.
"""


# Example of default constructor :

class GeekforGeeks:

    # default constructor
    def __init__(self):
        self.geek = "Python"

    # a method for printing data members
    def print_Geek(self):
        print(self.geek)


# creating object of the class
obj = GeekforGeeks()

# calling the instance method using the object obj
obj.print_Geek()

"""
Output:

Python
"""


# Example of the parameterized constructor :

class Addition:
    first = 0
    second = 0
    answer = 0

    # parameterized constructor
    def __init__(self, f, s):
        self.first = f
        self.second = s

    def display(self):
        print("First number = " + str(self.first))
        print("Second number = " + str(self.second))
        print("Addition of two numbers = " + str(self.answer))

    def calculate(self):
        self.answer = self.first + self.second


# creating object of the class
# this will invoke parameterized constructor
obj = Addition(1000, 2000)

# perform Addition
obj.calculate()

# display result
obj.display()

"""
Output : 

First number = 1000
Second number = 2000
Addition of two numbers = 3000
"""

# Destructors in Python

"""
Destructors are called when an object gets destroyed. 
In Python, destructors are not needed as much as in C++ because Python has a garbage collector that handles memory management automatically.

The __del__() method is a known as a destructor method in Python. 
It is called when all references to the object have been deleted i.e when an object is garbage collected. 

Syntax of destructor declaration : 
 

def __del__(self):
  # body of destructor

Note : A reference to objects is also deleted when the object goes out of reference or when the program ends. 

"""


# Example 1 : Here is the simple example of destructor. By using del keyword we deleted the all references of object ‘obj’, therefore destructor invoked automatically.

# Python program to illustrate destructor
class Employee:

    # Initializing
    def __init__(self):
        print('Employee created.')

    # Deleting (Calling destructor)
    def __del__(self):
        print('Destructor called, Employee deleted.')


obj = Employee()
del obj

"""
Employee created.
Destructor called, Employee deleted.
"""


# Note : The destructor was called after the program ended or when all the references to object are deleted i.e when the reference count becomes zero, not when object went out of scope.

# Example 2 :This example gives the explanation of above mentioned note. Here, notice that the destructor is called after the ‘Program End…’ printed.

# Python program to illustrate destructor

class Employee:

    # Initializing
    def __init__(self):
        print('Employee created')

    # Calling destructor
    def __del__(self):
        print("Destructor called")


def Create_obj():
    print('Making Object...')
    obj = Employee()
    print('function end...')
    return obj


print('Calling Create_obj() function...')
obj = Create_obj()
print('Program End...')

"""
Output: 
Calling Create_obj() function...
Making Object...
Employee created
function end...
Program End...
Destructor called
"""


# Example 3 : Now, consider the following example :

# Python program to illustrate destructor

class A:
    def __init__(self, bb):
        self.b = bb


class B:
    def __init__(self):
        self.a = A(self)

    def __del__(self):
        print("die")


def fun():
    b = B()


fun()

"""
Output:
 
die
"""

"""
In this example when the function fun() is called, it creates an instance of class B which passes itself to class A, which then sets a reference to class B and resulting in a circular reference.
Generally, Python’s garbage collector which is used to detect these types of cyclic references would remove it but in this example the use of custom destructor marks this item as “uncollectable”. 
Simply, it doesn’t know the order in which to destroy the objects, so it leaves them. Therefore, if your instances are involved in circular references they will live in memory for as long as the application run.
"""
