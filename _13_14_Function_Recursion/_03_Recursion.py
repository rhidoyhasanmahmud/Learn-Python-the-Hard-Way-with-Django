"""

The term Recursion can be defined as the process of defining something in terms of itself. In simple words,
it is a process in which a function calls itself directly or indirectly.

>> Advantages of using recursion

1. A complicated function can be split down into smaller sub-problems utilizing recursion.
2. Sequence creation is simpler through recursion than utilizing any nested iteration.
3. Recursive functions render the code look simple and effective.

>> Disadvantages of using recursion

1. A lot of memory and time is taken through recursive calls which makes it expensive for use.
2. Recursive functions are challenging to debug.
3. The reasoning behind recursion can sometimes be tough to think through.

>> Syntax

def func(): <--
              |
              | (recursive call)
              |
    func() ----

"""


# Example 1: A Fibonacci sequence is the integer sequence of 0, 1, 1, 2, 3, 5, 8….

# Program to print the fibonacci series up-to n_terms
# Recursive function
def recursive_fibonacci(n):
    if n <= 1:
        return n
    else:
        return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)


n_terms = 10

# check if the number of terms is valid
if n_terms <= 0:
    print("Invalid input ! Please input a positive value")
else:
    print("Fibonacci series:")
for i in range(n_terms):
    print(recursive_fibonacci(i))

"""
Output:

Fibonacci series:
0
1
1
2
3
5
8
13
21
34
"""


# Example 2: The factorial of 6 is denoted as 6! = 1*2*3*4*5*6 = 720.

# Program to print factorial of a number recursively.
# Recursive function
def recursive_factorial(n):
    if n == 1:
        return n
    else:
        return n * recursive_factorial(n - 1)


# user input
num = 6

# check if the input is valid or not
if num < 0:
    print("Invalid input ! Please enter a positive number.")
elif num == 0:
    print("Factorial of number 0 is 1")
else:
    print("Factorial of number", num, "=", recursive_factorial(num))

"""
Output:

Factorial of number 6 = 720
"""


# Head recursion Vs Tail recursion

# Tail recursions will not have any code statements after function calls
# and are generally at the end of the function declaration.
def tail(n, cnt):
    if n == 0:
        return
    else:
        print("CNT - ", cnt)
        print(n)
    cnt += 1
    tail(n - 1, cnt)


print(tail(10, 0))


# If a recursion has code statements to be executed after function call then it is a Head recursion.
def head(n, cnt):
    if n == 0:
        return
    else:
        cnt += 1
        head(n - 1, cnt)

    print("CNT", cnt)
    print(n)


print(head(10, 1))

# Which is better? [Head and Tail]

"""
Generally, tail recursions are always better. Even though they both have same time complexity 
and Auxiliary space, tail recursions takes an edge in terms of memory in function stack. 
Head recursions will wait in function stack memory until the post recursion code statements are executed 
which causes a latency in overall results, whereas tail recursions will be terminated in function 
stack over execution.

Link: https://res.cloudinary.com/practicaldev/image/fetch/s--Pfc6Kz3V--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/uploads/articles/zbcwhwt1e5j118uan6mz.jpg
"""
