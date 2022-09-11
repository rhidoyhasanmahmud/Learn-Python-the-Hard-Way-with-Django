"""
The continue statement is used inside a for loop or a while loop.
The continue statement skips the current iteration and starts the next one.
"""

"""
for index in range(n):
    if condition:
       continue
    # more code here


while condition1:
    if condition2:
        continue
    # more code here
"""

for index in range(10):
    if index % 2:
        continue

    print(index)

"""
0
2
4
6
8
"""

counter = 0
while counter < 10:
    counter += 1

    if not counter % 2:
        continue

    print(counter)

"""
1
3
5
7
9
"""

"""
Use the Python continue statement to skip the current iteration and start the next one.
"""
