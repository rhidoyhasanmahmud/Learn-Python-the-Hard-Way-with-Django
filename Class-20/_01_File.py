"""
>> Python File

Files are named locations on disk to store related information.
They are used to permanently store data in a non-volatile memory (e.g. hard disk).

Since Random Access Memory (RAM) is volatile (which loses its data when the computer is turned off),
we use files for future use of the data by permanently storing them.

When we want to read from or write to a file, we need to open it first.
When we are done, it needs to be closed so that the resources that are tied with the file are freed.
"""

# Opening Files in Python

"""
- Python has a built-in open() function to open a file. Python has a built-in open() function to open a file.

"""
fileObj = open("demofile.txt")
fileObj2 = open("H:/Python_Batch_3/Class-20/demofile.txt")

"""
r	Opens a file for reading. (default)
w	Opens a file for writing. Creates a new file if it does not exist or truncates the file if it exists.
x	Opens a file for exclusive creation. If the file already exists, the operation fails.
a	Opens a file for appending at the end of the file without truncating it. Creates a new file if it does not exist.
t	Opens in text mode. (default)
b	Opens in binary mode.
+	Opens a file for updating (reading and writing)
"""

fileObj3 = open("demofile.txt")  # equivalent to 'r' or 'rt'
fileObj4 = open("demofile.txt", 'w')  # write in text mode
fileObj5 = open("demofile.txt", 'r+b')  # read and write in binary mode

fileObj6 = open("demofile.txt", mode='r', encoding='utf-8')

# Closing Files in Python

"""
- When we are done with performing operations on the file, we need to properly close the file.
- Closing a file will free up the resources that were tied with the file. It is done using the close() method
- Python has a garbage collector to clean up unreferenced objects but we must not rely on it to close the file. 
"""

fileObj7 = open("demofile.txt", encoding='utf-8')
# perform file operations
fileObj7.close()

# A safer way is to use a try...finally block.

try:
    fileObj8 = open("demofile.txt", encoding='utf-8')
    # perform file operations
finally:
    fileObj8.close()

# We don't need to explicitly call the close() method. It is done internally.

with open("demofile.txt", encoding='utf-8') as fileObj9:
    # perform file operations
    print(fileObj9.read())

# Writing to Files in Python

"""
In order to write into a file in Python, we need to open it in write w, append a or exclusive creation x mode.
"""

with open("demofile.txt",'w',encoding = 'utf-8') as fileObj10:
   fileObj10.write("my first file\n")
   fileObj10.write("This file\n\n")
   fileObj10.write("contains three lines\n")

# Reading Files in Python

fileObj11 = open("demofile.txt",'r',encoding = 'utf-8')
print(fileObj11.read(4)) # read the first 4 data

print(fileObj11.tell()) # get the current file position

print(fileObj11.seek(0)) # bring file cursor to initial position

for line in fileObj11:
    print(line, end='')

fileObj12 = open("demofile.txt",'r',encoding = 'utf-8')
print(fileObj12.readline())
print(fileObj12.readlines())