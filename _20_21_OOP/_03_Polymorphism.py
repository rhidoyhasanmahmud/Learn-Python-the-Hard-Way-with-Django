"""
Polymorphism: The word polymorphism means having many forms.

In programming, polymorphism means the same function name (but different signatures) being used for different types.
The key difference is the data types and number of arguments used in function.
"""

# Example of inbuilt polymorphic functions:

# Python program to demonstrate in-built poly-morphic functions

# len() being used for a string
print(len("Python")) # 6

# len() being used for a list
print(len([10, 20, 30])) # 3

# Examples of user-defined polymorphic functions:

# A simple Python function to demonstrate
# Polymorphism

def add(x, y, z=0):
    return x + y + z


# Driver code
print(add(2, 3)) # 5
print(add(2, 3, 4)) # 9

# Polymorphism with class methods:

class Bangladesh():
    def capital(self):
        print("Dhaka is the capital of Bangladesh.")

    def language(self):
        print("Bangla is the most widely spoken language of Bangladesh.")

    def type(self):
        print("Bangladesh is a developing country.")


class USA():
    def capital(self):
        print("Washington, D.C. is the capital of USA.")

    def language(self):
        print("English is the primary language of USA.")

    def type(self):
        print("USA is a developed country.")


obj_ind = Bangladesh()
obj_usa = USA()

for country in (obj_ind, obj_usa):
    country.capital()
    country.language()
    country.type()

"""
Dhaka is the capital of Bangladesh.
Bangla is the most widely spoken language of Bangladesh.
Bangladesh is a developing country.
Washington, D.C. is the capital of USA.
English is the primary language of USA.
USA is a developed country.
"""

# Polymorphism with Inheritance:

"""
In Python, Polymorphism lets us define methods in the child class that have the same name as the methods in the parent class. 
In inheritance, the child class inherits the methods from the parent class. However, it is possible to modify a method in a child class that it has inherited from the parent class. This is particularly useful in cases where the method inherited from the parent class doesn’t quite fit the child class. In such cases, we re-implement the method in the child class. This process of re-implementing a method in the child class is known as Method Overriding.  
"""


class Bird:
    def intro(self):
        print("There are many types of birds.")


    def flight(self):
        print("Most of the birds can fly but some cannot.")


class sparrow(Bird):
    def flight(self):
        print("Sparrows can fly.")


class ostrich(Bird):
    def flight(self):
        print("Ostriches cannot fly.")


obj_bird = Bird()
obj_spr = sparrow()
obj_ost = ostrich()

obj_bird.intro()
obj_bird.flight()

obj_spr.intro()
obj_spr.flight()

obj_ost.intro()
obj_ost.flight()

"""
There are many types of birds.
Most of the birds can fly but some cannot.
There are many types of birds.
Sparrows can fly.
There are many types of birds.
Ostriches cannot fly.
"""
