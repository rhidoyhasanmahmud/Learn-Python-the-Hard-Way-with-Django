country = "Bangladesh"

country2 = "USA"

# Process - 1
print(country)  # Bangladesh
print(country2)  # USA

# Process - 2
print("Country is : ", country)  # Country is :  Bangladesh
print("Country2 is : ", country2)  # Country2 is :  USA

print("Country : ", country, country2)  # Country :  Bangladesh USA
print("Country : ", country, " and ", country2)  # Country :  Bangladesh  and  USA

print("Country: " + country + country2)  # Country: BangladeshUSA

# Process - 3

print("Country one is : {} and Country two is : {}".format(country, country2))
# Country one is : Bangladesh and Country two is : USA

print("Country one is : {1} and Country two is : {0}".format(country, country2))
# Country one is : USA and Country two is : Bangladesh

print("Country one is : {c1} and Country two is : {c2}".format(c1=country, c2=country2))
# Country one is : Bangladesh and Country two is : USA

# Process - 4

print(f'{country} and {country2}')  # Bangladesh and USA

# Process - 5
print("Country are  %s and %s" % (country, country2))  # Country are  Bangladesh and USA

"""
10.101010101010

10.10
"""

num = 10.101010101010
print("%f" % num) # 10.101010
print("%.3f" % num) # 10.101
