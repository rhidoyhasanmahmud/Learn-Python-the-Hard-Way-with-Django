language = "Java"
language2 = "Python"
print(language)

print("My first language is : ", language)  # My first language is :  Java

print("My second language is: %s" % language)  # My second language is: Java

num = 10.555555
print(num)
print(type(num))
print("%.2f" % num)  # 10.56

print("My fav. language :", language, ' and ', language2)  # My fav. language : Java  and  Python

print("My fav. language: %s and %s" % (language, language2))

# ------------------------------------------

num1 = 5
num2 = 3                
print(f'{num1} times {num2} is {num1 / num2:.2f}')  #2f means print to 2 decimal precision
#5 times 3 is 1.67


#explicit call format() method
number1 = 'One'
number2 = 'Two'
number3 = 'Three'

# default(implicit) order
default_order = "{}, {} and {}".format(number1,number2,number3)
print(default_order)
# One, Two and Three


# order using positional argument
positional_order = "{1}, {0} and {2}".format(number1,number2,number3)
print(positional_order)
# Two, One and Three


# order using keyword argument
keyword_order = "{i}, {j} and {k}".format(j=number1,k=number2,i=number3)
print(keyword_order)
# Three, One and Two
