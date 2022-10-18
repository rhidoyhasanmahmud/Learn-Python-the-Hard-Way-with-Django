"""
A variable is only available from inside the region it is created. This is called scope.
"""

"""
Local Scope: A variable created inside a function belongs to the local scope of that function, 
and can only be used inside that function.
"""


def getValue():
    x = 300
    print(x)


getValue()  # 300

"""
Function Inside Function: As explained in the example above, the variable x is not available outside the function, 
but it is available for any function inside the function:
"""


def getValueV2():
    x = 300

    def innerFunc():
        print(x)

    innerFunc()


getValueV2()  # 300

"""
Global Scope: 
A variable created in the main body of the Python code is a global variable and belongs to the global scope.

Global variables are available from within any scope, global and local.
"""
x = 300


def getValueV3():
    print(x)


getValueV3()
print(x)

"""
300
300
"""

"""
Global Keyword
If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.

The global keyword makes the variable global.
"""


def myfunc():
    global x
    x = 300


myfunc()

print(x)
