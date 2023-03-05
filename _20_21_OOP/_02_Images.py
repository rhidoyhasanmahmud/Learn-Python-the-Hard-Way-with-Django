"""
>> Inheritance

Inheritance is the capability of one class to derive or inherit the properties from another class.

Benefits of inheritance are:

- It represents real-world relationships well.
- It provides the reusability of a code. We don’t have to write the same code again and again. Also, it allows us to add more features to a class without modifying it.
- It is transitive in nature, which means that if class B inherits from another class A, then all the subclasses of B would automatically inherit from class A.

> Python Inheritance Syntax

Class BaseClass:
    {Body}
Class DerivedClass(BaseClass):
    {Body}
"""


# Creating a Parent Class [Creating a Person class with Display methods.]

# A Python program to demonstrate inheritance

class Person(object):

    # Constructor
    def __init__(self, name, id):
        self.name = name
        self.id = id

    # To check if this person is an employee
    def Display(self):
        print(self.name, self.id)


# Driver code
emp = Person("Hasan", 102)  # An Object of Person
emp.Display()

"""
Output:

Hasan 102
"""


# Creating a Child Class

class Emp(Person):

    def Print(self):
        print("Emp class called")


Emp_details = Emp("Hasan", 103)

# calling parent class function
Emp_details.Display()

# Calling child class function
Emp_details.Print()

"""
Output:

Hasan 103
Emp class called
"""


# Example of Inheritance in Python

# A Python program to demonstrate inheritance

# Base or Super class. Note object in bracket.
# (Generally, object is made ancestor of all classes)
# In Python 3.x "class Person" is
# equivalent to "class Person(object)"


class Person(object):

    # Constructor
    def __init__(self, name):
        self.name = name

    # To get name
    def getName(self):
        return self.name

    # To check if this person is an employee
    def isEmployee(self):
        return False


# Inherited or Subclass (Note Person in bracket)
class Employee(Person):

    # Here we return true
    def isEmployee(self):
        return True


# Driver code
emp = Person("Hasan Mahmud 1")  # An Object of Person
print(emp.getName(), emp.isEmployee())

emp = Employee("Hasan Mahmud 2")  # An Object of Employee
print(emp.getName(), emp.isEmployee())

"""
Output:

Hasan Mahmud 1 False
Hasan Mahmud 2 True
"""


# Subclassing (Calling constructor of parent class)

# Python code to demonstrate how parent constructors
# are called.

# parent class
class Person(object):

    # __init__ is known as the constructor
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print(self.name)
        print(self.idnumber)


# child class


class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post

        # invoking the __init__ of the parent class
        Person.__init__(self, name, idnumber)


# creation of an object variable or an instance
a = Employee('Hasan', 886012, 200000, "SDE")

# calling a function of the class Person using its instance
a.display()
"""
Output:

Hasan
886012
"""

# Python program to demonstrate error if we forget to invoke __init__() of the parent

"""
class A:
    def __init__(self, n='Rahul'):
        self.name = n


class B(A):
    def __init__(self, roll):
        self.roll = roll


object = B(23)
print(object.name) # AttributeError: 'B' object has no attribute 'name'
"""

"""
>> Different types of Inheritance:

> Single inheritance: When a child class inherits from only one parent class, it is called single inheritance. We saw an example above.
> Multiple inheritances: When a child class inherits from multiple parent classes, it is called multiple inheritances. 
"""


# Python program to demonstrate
# single inheritance

# Base class
class Parent:
    def func1(self):
        print("This function is in parent class.")


# Derived class


class Child(Parent):
    def func2(self):
        print("This function is in child class.")


# Driver's code
object = Child()
object.func1()
object.func2()

"""
Output:
This function is in parent class.
This function is in child class.
"""


# ------------------

# Python program to demonstrate
# multiple inheritance

# Base class1
class Mother:
    mothername = ""

    def mother(self):
        print(self.mothername)


# Base class2


class Father:
    fathername = ""

    def father(self):
        print(self.fathername)


# Derived class


class Son(Mother, Father):
    def parents(self):
        print("Father :", self.fathername)
        print("Mother :", self.mothername)


# Driver's code
s1 = Son()
s1.fathername = "Tipu"
s1.mothername = "Beauty"
s1.parents()

"""
Output:

Father : Tipu
Mother : Beauty
"""
# -------------

"""
Multilevel Inheritance : In multilevel inheritance, features of the base class and the derived class are 
                         further inherited into the new derived class. This is similar to a relationship 
                         representing a child and a grandfather. 
"""


# Python program to demonstrate
# multilevel inheritance

# Base class


class Grandfather:

    def __init__(self, grandfathername):
        self.grandfathername = grandfathername


# Intermediate class


class Father(Grandfather):
    def __init__(self, fathername, grandfathername):
        self.fathername = fathername

        # invoking constructor of Grandfather class
        Grandfather.__init__(self, grandfathername)


# Derived class


class Son(Father):
    def __init__(self, sonname, fathername, grandfathername):
        self.sonname = sonname

        # invoking constructor of Father class
        Father.__init__(self, fathername, grandfathername)

    def print_name(self):
        print('Grandfather name :', self.grandfathername)
        print("Father name :", self.fathername)
        print("Son name :", self.sonname)


#  Driver code
s1 = Son('S', 'F', 'GF')
print(s1.grandfathername)
s1.print_name()
"""
Output: 

GF
Grandfather name : GF
Father name : F
Son name : S
"""

"""
Hierarchical Inheritance:  When more than one derived class are created from a single base this type of inheritance 
    is called hierarchical inheritance. In this program, we have a parent (base) class and two child (derived) classes.
"""


# Python program to demonstrate
# Hierarchical inheritance


# Base class
class Parent:
    def func1(self):
        print("This function is in parent class.")


# Derived class1


class Child1(Parent):
    def func2(self):
        print("This function is in child 1.")


# Derivied class2


class Child2(Parent):
    def func3(self):
        print("This function is in child 2.")


# Driver's code
object1 = Child1()
object2 = Child2()
object1.func1()
object1.func2()
object2.func1()
object2.func3()

"""
Output:

This function is in parent class.
This function is in child 1.
This function is in parent class.
This function is in child 2.
"""

# Hybrid Inheritance: Inheritance consisting of multiple types of inheritance is called hybrid inheritance.

# Python program to demonstrate
# hybrid inheritance


class School:
    def func1(self):
        print("This function is in school.")


class Student1(School):
    def func2(self):
        print("This function is in student 1. ")


class Student2(School):
    def func3(self):
        print("This function is in student 2.")


class Student3(Student1, School):
    def func4(self):
        print("This function is in student 3.")


# Driver's code
object = Student3()
object.func1()
object.func2()

"""
Output:

This function is in school.
This function is in student 1.
"""
