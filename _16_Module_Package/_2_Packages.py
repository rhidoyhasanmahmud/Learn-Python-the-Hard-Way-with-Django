"""
>> Python mypackages

- A python package is a collection of modules.
- Modules that are related to each other are mainly put in the same package.

<Any Python file, whose name is the module’s name property without the .py extension, is a module.>

A package is a directory of Python modules that contains an additional __init__.py file,
which distinguishes a package from a directory that is supposed to contain multiple Python scripts.

Packages can be nested to multiple depths if each corresponding directory contains its own __init__.py file.
"""

"""
Creating Package
Let’s create a package named mypackages that will contain two modules mod1 and mod2. 
To create this module follow the below steps – 

1. Create a folder named mypackages.
2. Inside this folder create an empty Python file i.e. __init__.py
3. Then create two modules mod1 and mod2 in this folder.
"""

"""
The hierarchy of the our package looks like this – 

mypackages
|
|
---__init__.py
|
|
---mod1.py
|
|
---mod2.py
"""

"""
__init__.py helps the Python interpreter to recognise the folder as package.

It also specifies the resources to be imported from the modules. 

If the __init__.py is empty this means that all the functions of the modules will be imported.

We can also specify the functions from each module to be made available.

This __init__.py will only allow the gfg and sum functions from the mod1 and mod2 modules to be imported.

Syntax:

import package_name.module_name
"""

# Import Modules from a Package

from mypackages import Mod1  # from mypckg.mod1 import gfg
from mypackages import Mod2  # from mypckg.mod2 import sum

Mod1.gfg()  # Welcome to GFG
res = Mod2.sum(1, 2)  # 3
print(res)
