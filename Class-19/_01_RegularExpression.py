"""
A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.

RegEx can be used to check if a string contains the specified search pattern.

"""

# RegEx Functions

"""
findall	Returns a list containing all matches
search	Returns a Match object if there is a match anywhere in the string
split	Returns a list where the string has been split at each match
sub	    Replaces one or many matches with a string
"""

# The findall() function returns a list containing all matches.

import re

txt = "We Love Python"
x = re.findall("on", txt)
print(x)  # ['on']

# The search() function searches the string for a match, and returns a Match object if there is a match.
# If there is more than one match, only the first occurrence of the match will be returned:

txt = "We Love Python"
x = re.search("o", txt)
x2 = re.search("Java", txt)

print("First Located in position:", x.start())  # First Located in position: 4
# print("First Located in position:", x2.start())  # First Located in position: None

# The split() Function

txt = "Python Java C++"
x = re.split("\s", txt)
print(x)  # ['Python', 'Java', 'C++']

# The sub() function replaces the matches with the text of your choice:

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)  # The9rain9in9Spain

"""
.span() returns a tuple containing the start-, and end positions of the match.
.string returns the string passed into the function
.group() returns the part of the string where there was a match
"""
# Search for an upper case "S" character in the beginning of a word, and print its position:
txt = "The rain in Spain"
x = re.search("Sp", txt)
print(x.span())

"""
[]	A set of characters	"[a-m]"	
\	Signals a special sequence (can also be used to escape special characters)	"\d"	
.	Any character (except newline character)	"he..o"	
^	Starts with	"^hello"	
$	Ends with	"planet$"	
*	Zero or more occurrences	"he.*o"	
+	One or more occurrences	"he.+o"	
?	Zero or one occurrences	"he.?o"	
{}	Exactly the specified number of occurrences	"he.{2}o"	
|	Either or	"falls|stays"	
()	Capture and group	 
"""

"""
\A	Returns a match if the specified characters are at the beginning of the string	"\AThe"	
\b	Returns a match where the specified characters are at the beginning or at the end of a word
(the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\bain"
r"ain\b"
	
\B	Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
(the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\Bain"
r"ain\B"
	
\d	Returns a match where the string contains digits (numbers from 0-9)	"\d"	
\D	Returns a match where the string DOES NOT contain digits	"\D"	
\s	Returns a match where the string contains a white space character	"\s"	
\S	Returns a match where the string DOES NOT contain a white space character	"\S"	
\w	Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)	"\w"	
\W	Returns a match where the string DOES NOT contain any word characters	"\W"	
\Z	Returns a match if the specified characters are at the end of the string	"Spain\Z"
"""
