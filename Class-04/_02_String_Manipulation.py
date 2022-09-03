languageName = "Python"
languageName2 = 'Java'

print(type(languageName))  # <class 'str'>
print(type(languageName2))  # <class 'str'>

# [Example] -> 'Python' is my primary language

# [Wrong Approach] str = ''Python' is my primary language.'

str = "'Python' is my primary language."
print(str)  # 'Python' is my primary language.

str2 = '\'Python\' is my primary language.'
print(str2)  # 'Python' is my primary language.

# [Example] -> "Python" is my primary language

str3 = '"Python" is my primary language.'
print(str3)

str4 = "\"Python\" is my primary language."
print(str4)

# [Example] -> \Python\ is my primary language

str5 = "\\Python\\ is my primary language."
print(str5)

str6 = '\\Python\\ is my primary language.'
print(str6)

str7 = "Java is my second language.\nPython is my First Language."  # \n -> New Line
print(str7, end="")  # "\n"

str8 = "Java is my second language.\tPython is my First Language."  # \t -> tab
print(str8)