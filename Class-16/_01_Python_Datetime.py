"""
>> Python datetime

- Python has a module named datetime to work with dates and times.
"""
# Example 1: Get Current Date and Time

import datetime

datetime_object = datetime.datetime.now()
print(datetime_object)  # 2022-10-18 20:08:25.951993

# Example 2: Get Current Date

date_object = datetime.date.today()
print(date_object)  # 2022-10-18

"""
>> What's inside datetime?

- We can use dir() function to get a list containing all attributes of a module.
"""

print(dir(datetime))

# ['MAXYEAR', 'MINYEAR', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'date', 'datetime', 'datetime_CAPI', 'sys', 'time', 'timedelta', 'timezone', 'tzinfo']

"""
Commonly used classes in the datetime module are:

- date Class
- time Class
- datetime Class
- timedelta Class
"""

# Example 3: Date object to represent a date

d = datetime.date(2019, 4, 13)
print(d)  # 2019-04-13

# Example 4: Print today's year, month and day

from datetime import date

# date object of today's date
today = date.today()

print("Current year:", today.year)  # Current year: 2022
print("Current month:", today.month)  # Current month: 10
print("Current day:", today.day)  # Current day: 18

# Example 5: Print hour, minute, second and microsecond

from datetime import time

a = time(11, 34, 56)

print("hour =", a.hour)  # hour = 11
print("minute =", a.minute)  # minute = 34
print("second =", a.second)  # second = 56
print("microsecond =", a.microsecond)  # microsecond = 0

# Example 6: Format date using strftime()


from datetime import datetime

# current date and time
now = datetime.now()

t = now.strftime("%H:%M:%S")
print("time:", t)  # time: 20:14:44

s1 = now.strftime("%m/%d/%Y, %H:%M:%S")
# mm/dd/YY H:M:S format
print("s1:", s1)  # s1: 10/18/2022, 20:14:44

s2 = now.strftime("%d/%m/%Y, %H:%M:%S")
# dd/mm/YY H:M:S format
print("s2:", s2)  # s2: 18/10/2022, 20:14:44
