# RegEx Module

import re

# Another example

txt = "The rain in Spain"

x = re.search("^The.*Spain$", txt) # Check if the string starts with "The" and ends with "Spain"

if x:
  
  print("YES! We have a match!")

else:
  
  print("No match")

# RegEx Functions
# Returns a list containing all matches

txt = "The rain in Spain"

x = re.findall("ai", txt)

print(x)

# Returns a Match object if there is a match anywhere in the string

txt = "The rain in Spain"

x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())

# Returns a list where the string has been split at each match

txt = "The rain in Spain"

x = re.split("\s", txt)

print(x)

# Replaces one or many matches with a string

txt = "The rain in Spain"

x = re.sub("\s", "9", txt)

print(x)

# Metacharacters
# A set of characters	, "[a-m]"

txt = "The rain in Spain"

x = re.findall("[a-m]", txt) # Find all lower case characters alphabetically between "a" and "m":

print(x)

# Signals a special sequence (can also be used to escape special characters)	, "\d"

txt = "That will be 59 dollars"

x = re.findall("\d", txt) # Find all digit characters:

print(x)

# Any character (except newline character)	, "he..o"

txt = "hello planet"

x = re.findall("he..o", txt) # Search for a sequence that starts with "he", followed by two (any) characters, and an "o":

print(x)

# Starts with	, "^hello"

txt = "hello planet"

x = re.findall("^hello", txt) # Check if the string starts with 'hello':

if x:
  
  print("Yes, the string starts with 'hello'")

else:
  
  print("No match")

# Ends with	, "planet$"

txt = "hello planet"

x = re.findall("planet$", txt) # Check if the string ends with 'planet':

if x:
  
  print("Yes, the string ends with 'planet'")

else:
  
  print("No match")

# Zero or more occurrences	, "he.*o"

txt = "hello planet"

x = re.findall("he.*o", txt) # Search for a sequence that starts with "he", followed by 0 or more  (any) characters, and an "o":

print(x)

# One or more occurrences	, "he.+o"

txt = "hello planet"

x = re.findall("he.+o", txt) # Search for a sequence that starts with "he", followed by 1 or more  (any) characters, and an "o":

print(x)

# Zero or one occurrences	, "he.?o"

txt = "helo planet"

x = re.findall("he.?o", txt) # Search for a sequence that starts with "he", followed by 0 or 1  (any) character, and an "o":

print(x) 

# Exactly the specified number of occurrences	, "he.{2}o"

txt = "hello planet"

x = re.findall("he.{2}o", txt) # Search for a sequence that starts with "he", followed excactly 2 (any) characters, and an "o":

print(x)

# Either or  	, "falls|stays"

txt = "The rain in Spain falls mainly in the plain!"

x = re.findall("falls|stays", txt) # Check if the string contains either "falls" or "stays":

print(x)

if x:
  
  print("Yes, there is at least one match!")

else:
  
  print("No match")

# Special Sequences
# Returns a match if the specified characters are at the beginning of the string	, "\AThe"

txt = "The rain in Spain"



x = re.findall("\AThe", txt) # Check if the string starts with "The":

print(x)

if x:

  print("Yes, there is a match!")

else:

  print("No match")

# Returns a match where the specified characters are at the beginning or at the end of a word
# (the "r" in the beginning is making sure that the string is being treated as a "raw string")
# r"\bain"

txt = "The rain in Spain"

x = re.findall(r"\bain", txt) # Check if "ain" is present at the beginning of a WORD:

print(x)

if x:

  print("Yes, there is at least one match!")

else:

  print("No match")

# Another example
# r"ain\b"

txt = "The rain in Spain"

x = re.findall(r"ain\b", txt)  # Check if "ain" is present at the end of a WORD:

print(x)

if x:

  print("Yes, there is at least one match!")

else:

  print("No match")

# 	Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
# (the "r" in the beginning is making sure that the string is being treated as a "raw string")
# r"\Bain"

txt = "The rain in Spain"

x = re.findall(r"\Bain", txt) # Check if "ain" is present, but NOT at the beginning of a word:

print(x)

if x:

  print("Yes, there is at least one match!")

else:

  print("No match")

# r"ain\B"

txt = "The rain in Spain"



x = re.findall(r"ain\B", txt) # Check if "ain" is present, but NOT at the end of a word:

print(x)

if x:

  print("Yes, there is at least one match!")

else:

  print("No match")

# Returns a match where the string contains digits (numbers from 0-9)	, "\d"

txt = "The rain in Spain 9"

x = re.findall("\d", txt) # Check if the string contains any digits (numbers from 0-9):

print(x)

if x:

  print("Yes, there is at least one match!")

else:

  print("No match")

# Returns a match where the string DOES NOT contain digits	, "\D"

txt = "The rain in Spain"

x = re.findall("\D", txt) # Return a match at every no-digit character:

print(x)

if x:

  print("Yes, there is at least one match!")

else:

  print("No match")

# Returns a match where the string contains a white space character	, "\s"

txt = "The rain in Spain"

x = re.findall("\s", txt) # Return a match at every white-space character:

print(x)

if x:

  print("Yes, there is at least one match!")

else:

  print("No match")

# Returns a match where the string DOES NOT contain a white space character , 	"\S"

txt = "The rain in Spain"

x = re.findall("\S", txt) # Return a match at every NON white-space character:

print(x)

if x:

  print("Yes, there is at least one match!")

else:

  print("No match")

# Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)	, "\w"

txt = "The rain in_Spain 9"

x = re.findall("\w", txt) # Return a match at every word character (characters from a to Z, digits from 0-9, and the underscore _ character):

print(x)

if x:

  print("Yes, there is at least one match!")

else:

  print("No match")

# Returns a match where the string DOES NOT contain any word characters	, "\W"

txt = "! The rain in Spain ?"

x = re.findall("\W", txt) # Return a match at every NON word character (characters NOT between a and Z. Like "!", "?" white-space etc.):

print(x)

if x:

  print("Yes, there is at least one match!")

else:

  print("No match")

# Returns a match if the specified characters are at the end of the string	, "Spain\Z"

txt = "The rain in Spain"

x = re.findall("Spain\Z", txt) # Check if the string ends with "Spain":

print(x)

if x:

  print("Yes, there is a match!")

else:

  print("No match")

# Sets
# Returns a match where one of the specified characters (a, r, or n) is present

txt = "The rain in Spain"

x = re.findall("[arn]", txt) # Check if the string has any a, r, or n characters:

print(x)

if x:

  print("Yes, there is at least one match!")

else:

  print("No match")

# Returns a match for any lower case character, alphabetically between a and n

txt = "The rain in Spain"

x = re.findall("[a-n]", txt) # Check if the string has any characters between a and n:

print(x)

if x:

  print("Yes, there is at least one match!")

else:

  print("No match")

# Returns a match for any character EXCEPT a, r, and n

txt = "The rain in Spain"

#Check if the string has other characters than a, r, or n:

x = re.findall("[^arn]", txt)

print(x)

if x:

  print("Yes, there is at least one match!")

else:

  print("No match")

# Returns a match where any of the specified digits (0, 1, 2, or 3) are present

txt = "The rain in Spain 2"

x = re.findall("[0123]", txt) # Check if the string has any 0, 1, 2, or 3 digits:

print(x)

if x:

  print("Yes, there is at least one match!")

else:

  print("No match")

# Returns a match for any digit between 0 and 9

txt = "8 times before 11:45 AM"

x = re.findall("[0-9]", txt) # Check if the string has any digits:

print(x)

if x:

  print("Yes, there is at least one match!")

else:

  print("No match")

# Returns a match for any two-digit numbers from 00 and 59

txt = "8 times before 11:45 AM"

x = re.findall("[0-5][0-9]", txt) # Check if the string has any two-digit numbers, from 00 to 59:

print(x)

if x:

  print("Yes, there is at least one match!")

else:

  print("No match")

# Returns a match for any character alphabetically between a and z, lower case OR upper case

txt = "8 times before 11:45 AM"

x = re.findall("[a-zA-Z]", txt) # Check if the string has any characters from a to z lower case, and A to Z upper case:

print(x)

if x:

  print("Yes, there is at least one match!")

else:

  print("No match")

# In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string

txt = "8 times + before 11:45 AM"

x = re.findall("[+]", txt) # Check if the string has any + characters:

print(x)

if x:

  print("Yes, there is at least one match!")

else:

  print("No match")

# The findall() Function

txt = "The rain in Spain"

x = re.findall("ai", txt)

print(x)

# The search() Function

txt = "The rain in Spain"

x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())

# The split() Function

txt = "The rain in Spain"

x = re.split("\s", txt)

print(x)

# Another example

txt = "The rain in Spain"

x = re.split("\s", txt, 1)

print(x)

# The sub() Function

txt = "The rain in Spain"

x = re.sub("\s", "9", txt)

print(x)

# Another example

txt = "The rain in Spain"

x = re.sub("\s", "9", txt, 2)

print(x)

# Match Object

txt = "The rain in Spain"

x = re.search("ai", txt)

print(x) #this will print an object

# Another example - span - returns a tuple containing the start-, and end positions of the match.

txt = "The rain in Spain"

x = re.search(r"\bS\w+", txt)

print(x.span())

# Another example - string - returns the string passed into the function

txt = "The rain in Spain"

x = re.search(r"\bS\w+", txt)

print(x.string)

# Another example - group - returns the part of the string where there was a match

txt = "The rain in Spain"

x = re.search(r"\bS\w+", txt)

print(x.group())


