"""
>> Abstract Classes in Python

An abstract class can be considered as a blueprint for other classes. It allows you to create a set of methods that must be created within any child classes built from the abstract class. A class which contains one or more abstract methods is called an abstract class. An abstract method is a method that has a declaration but does not have an implementation. While we are designing large functional units we use an abstract class. When we want to provide a common interface for different implementations of a component, we use an abstract class.

> Why use Abstract Base Classes :

By defining an abstract base class, you can define a common Application Program Interface(API) for a set of subclasses. This capability is especially useful in situations where a third-party is going to provide implementations, such as with plugins, but can also help you when working in a large team or with a large code-base where keeping all classes in your mind is difficult or not possible.

> How Abstract Base classes work :

By default, Python does not provide abstract classes. Python comes with a module that provides the base for defining Abstract Base classes(ABC) and that module name is ABC. ABC works by decorating methods of the base class as abstract and then registering concrete classes as implementations of the abstract base. A method becomes abstract when decorated with the keyword @abstractmethod. For Example –
"""

# Python program showing
# abstract base class work

from abc import ABC, abstractmethod


class Polygon(ABC):

    @abstractmethod
    def noofsides(self):
        pass


class Triangle(Polygon):

    # overriding abstract method
    def noofsides(self):
        print("I have 3 sides")


class Pentagon(Polygon):

    # overriding abstract method
    def noofsides(self):
        print("I have 5 sides")


class Hexagon(Polygon):

    # overriding abstract method
    def noofsides(self):
        print("I have 6 sides")


class Quadrilateral(Polygon):

    # overriding abstract method
    def noofsides(self):
        print("I have 4 sides")


# Driver code
R = Triangle()
R.noofsides()

K = Quadrilateral()
K.noofsides()

R = Pentagon()
R.noofsides()

K = Hexagon()
K.noofsides()

"""
Output: 
 

I have 3 sides
I have 4 sides
I have 5 sides
I have 6 sides
"""

# Python program showing
# abstract base class work

from abc import ABC, abstractmethod


class Animal(ABC):

    def move(self):
        pass


class Human(Animal):

    def move(self):
        print("I can walk and run")


class Snake(Animal):

    def move(self):
        print("I can crawl")


class Dog(Animal):

    def move(self):
        print("I can bark")


class Lion(Animal):

    def move(self):
        print("I can roar")


# Driver code
R = Human()
R.move()

K = Snake()
K.move()

R = Dog()
R.move()

K = Lion()
K.move()

"""
Output: 
 

I can walk and run
I can crawl
I can bark
I can roar
"""

# Implementation Through Subclassing :

# Python program showing
# implementation of abstract
# class through subclassing

import abc


class parent:
    def geeks(self):
        pass


class child(parent):
    def geeks(self):
        print("child class")


# Driver code
print(issubclass(child, parent))
print(isinstance(child(), parent))

"""
Output: 
 

True
True
"""

# Concrete Methods in Abstract Base Classes :


# Python program invoking a
# method using super()

import abc
from abc import ABC, abstractmethod


class R(ABC):
    def rk(self):
        print("Abstract Base Class")


class K(R):
    def rk(self):
        super().rk()
        print("subclass ")


# Driver code
r = K()
r.rk()

"""
Output: 
 

Abstract Base Class
subclass
"""