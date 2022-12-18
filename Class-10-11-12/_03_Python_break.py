"""
Sometimes, you wan to terminate a for loop or a while loop prematurely
regardless of the results of the conditional tests.
In these cases, you can use the break statement:
"""

"""
for index in range(n):
    # more code here 
    if condition:
        break
"""

for index in range(0, 10):
    print(index)
    if index == 3:
        break

"""
0
1
2
3
"""

"""
while condition:
    # more code
    if condition:
        break
"""

while True:
    color = input('Enter your favorite color:')
    if color.lower() == 'quit':
        break
"""
Enter your favorite color:red
Enter your favorite color:green
Enter your favorite color:blue
Enter your favorite color:quit
"""

"""
Use the Python break statement to terminate a for loop or a while loop prematurely.
"""
