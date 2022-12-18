# [01] How to Take Input from User in Python

"""
Sometimes a developer might want to take user input at some point in the program.
To do this Python provides an input() function.

Syntax:
input('prompt')

where prompt is an optional string that is displayed on the string at the time of taking input.
"""

# [Example 1] Python get user input with a message

# Taking input from the user
name = input("Enter your name: ")

# Output
print("Hello, " + name)
print(type(name))

# [Example 2] Integer input in Python

# Taking input from the user as integer
num = int(input("Enter a number: "))

add = num + 1

# Output
print(add)

# [02] How to take Multiple Inputs in Python

# we can take multiple inputs of the same data type at a time in python, using map() method in python.

a, b, c = map(int, input("Enter the Numbers : ").split())  # Enter the Numbers : 10 10 10
print("The Numbers are : ", end=" ")
print(a, b, c)

# [03] How to Display Output in Python

"""
Python provides the print() function to display output to the standard output devices. 

Syntax: print(value(s), sep= ‘ ‘, end = ‘\n’, file=file, flush=flush)

Parameters:

value(s)        : Any value, and as many as you like. Will be converted to string before printed
sep=’separator’ : (Optional) Specify how to separate the objects, if there is more than one.Default :’ ‘
end=’end’       : (Optional) Specify what to print at the end.Default : ‘\n’
file            : (Optional) An object with a write method. Default :sys.stdout
flush           : (Optional) A Boolean, specifying if the output is flushed (True) or buffered (False). Default: False
Returns         : It returns output to the screen.
"""

# [Example 01] Python Print Output

# Python program to demonstrate
# print() method
print("PYTHON")

# code for disabling the softspace feature
print('P', 'Y', 'T', 'H', 'O', 'N')

# [Example 02] Python Print output with custom sep and end parameter

# Python program to demonstrate
# print() method
print("PYTHON", end="@")

# code for disabling the softspace feature
print('P', 'Y', 'T', 'H', 'O', 'N', sep="#")

# [04] Formatting Output

country = "Bangladesh"
country_2 = "USA"

# Process - 01
print(country)
print(country_2)
print("-------------------------------")

# Process - 02
print("Country is : ", country)
print("Country_2 is : ", country_2)
print("-------------------------------")

# Process - 03
print("Country is: ", country, " and ", country_2)
print("-------------------------------")

# Process - 04
print("Country one is : {} and Country two is: {}".format(country, country_2))
print("Country one is : {1} and Country two is: {0}".format(country, country_2))
print("Country one is : {c1} and Country two is: {c2}".format(c1=country, c2=country_2))
print("-------------------------------")

# Process - 05
print(f'Country are : {country} and {country_2}')
print(f"Country are : {country} and {country_2}")
print("-------------------------------")

# Process - 06
"""
We can use ‘%’ operator. % values are replaced with zero or more value of elements. 
The formatting using % is similar to that of ‘printf’ in the C programming language.

%d – integer
%f – float
%s – string
%x – hexadecimal
%o – octal
"""
"""
num = 10.1010101010101010
>> Num is : 10.10
----------------------------
%f -> Floating 
%s -> String 
%d -> Integer 
"""
num = 10.1010101010101010
print("%.1f" % num)
print("%.8f" % num)

num1 = 10
print("The Number is: %d" % num1)

language = "Python"
print("%s" % language)

print("Language is %s and Number is %.3f" % (language, num))
print("-------------------------------")
