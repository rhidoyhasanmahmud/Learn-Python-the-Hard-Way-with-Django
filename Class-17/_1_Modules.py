"""
>> Python Modules

- Modules are simply files with the “. py” extension containing Python code that can be imported
  inside another Python Program.

- In simple terms, we can consider a module to be the same as a code library or a
  file that contains a set of functions that you want to include in your application.

- A module allows you to logically organize your Python code.

- Grouping related code into a module makes the code easier to understand and use.

- A module is a Python object with arbitrarily named attributes that you can bind and reference.

- Simply, a module is a file consisting of Python code.
  A module can define functions, classes and variables.
  A module can also include runnable code.
"""
"""
>>  The import Statement

You can use any Python source file as a module by executing an import statement in some other Python source file. 

The import has the following syntax −
import module1[, module2[,... moduleN]

"""
import Common_File_Module as module

print(module.checkEvenOrOdd(10))  # Even

"""
>> The from...import Statement

Python's from statement lets you import specific attributes from a module into the current namespace.

The from...import has the following syntax −
from modname import name1[, name2[, ... nameN]]

from modname import *

"""

from Common_File_Module import checkEvenOrOdd
print(checkEvenOrOdd(21)) # Odd