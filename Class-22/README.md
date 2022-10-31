# Intro OOP

Object-Oriented Programming System is the programming technique to write programs based on the real world objects.

![A test image](images/java object.png)

# What is the difference between Procedural programming and OOPS?

1. A procedural language is based on functions object-oriented language is based on real-world objects.
2. Procedural language gives importance to the sequence of function execution 
   but object-oriented language gives importance on states and behaviors of the objects.
3. Procedural language exposes the data to the entire program but object-oriented language encapsulates the data.
4. Procedural language follows a top-down programming paradigm but object-oriented language follows a bottom-up programming paradigm.
5. A procedural language is complex in nature so it is difficult to modify, extend and maintain 
   but an object-oriented language is less complex in nature so it is easier to modify, extend and maintain.
6. Procedural language provides less scope of code reuse but object-oriented language provides more scope of code reuse.

# Object

The Object is the real-time entity having some state and behavior. 

I found various Object Definitions:
1. An object is a real-world entity.
2. An object is a runtime entity.
3. The object is an entity which has state and behavior.
4. The object is an instance of a class.

#### Real-world examples

> Dogs have state (name, color, breed, hungry) and behavior (barking, fetching, wagging tail). 
Chair, Bike, Marker, Pen, Table, Car, Book, Apple, Bag etc. It can be physical or logical (tangible and intangible).

> Bicycles also have state (current gear, current pedal cadence, current speed) and behavior (changing gear, changing pedal cadence, applying brakes).

# Bundling code into individual software objects provides a number of benefits, including:

1. Modularity: The source code for an object can be written and maintained independently of the source code for other objects. Once created, an object can be easily passed around inside the system.

2. Information-hiding: By interacting only with an object's methods, the details of its internal implementation remain hidden from the outside world.

3. Code re-use: If an object already exists (perhaps written by another software developer), you can use that object in your program. This allows specialists to implement/test/debug complex, task-specific objects, which you can then trust to run in your own code.

   4. Pluggability and debugging ease: If a particular object turns out to be problematic, you can simply remove it from your application and plug in a different object as its replacement. This is analogous to fixing mechanical problems in the real world. If a bolt breaks, you replace it, not the entire machine.
