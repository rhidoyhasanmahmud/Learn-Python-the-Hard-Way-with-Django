"""
Python while statement allows you to execute a code block repeatedly as long as a condition is True.
"""
"""
while condition:  
   body
"""

max = 5
counter = 0

while counter < max:
    print(counter)
    counter += 1

"""
0
1
2
3
4
"""

command = ''

while command.lower() != 'quit':
    command = input('>')
    print(f"Print: {command}")
"""
>Hi
Print: Hi
>Python while
Print: Python while
>quit
Print: quit
"""

"""
Use the Python while loop statement to execute a code block as long as a condition is True.
"""
