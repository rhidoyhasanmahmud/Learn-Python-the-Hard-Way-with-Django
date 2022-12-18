lang = "Python"
lang2 = "Java"

language = lang + lang2  # PythonJava
print(language)

# Python-Java

language2 = lang + "-" + lang2  # Python-Java
print(language2)

language3 = "-".join((lang, lang2, language2))  # Python-Java
print(language3)

print(type("1233"))  # <class 'str'>
