country = "Bangladesh"

country2 = 'India'

# Process - 1
print(country)
print(country2)

# Process - 2

print("Country is :", country)
print("Country2 is :", country2)

print("Country : ", country, country2)
print("Country: " + country + " and " + country2)
print("Country: ", country, " and ", country2)

print("Country:" + country)

"""
"Country: " 
+ [Concate]
country 
+ 
" and " 
+ 
country
"""
# print("Country" + 1) # TypeError: can only concatenate str (not "int") to str
print("Country: ", 1)

# Process - 3

print("Country one is: {} and Country two is: {}".format(country, country2))
print("Country one is: {2} and Country two is: {0}".format(country, country2, "USA"))
print("Country one is: {c1} and Country two is: {c2}".format(c1=country, c2=country2))
print("One is {} and Two is: {}".format(1, "Two"))

# Process - 4
num = 1
print(f'{country} and {country2} and {num}')

# Process - 5
num = 10.10101010101010  # 10.101
print(num)
print("%f" % num)
print("%.7f" % num)

print("Country are %s and %s" % (country, country2))

num2 = 10
print("%d" % num2)
