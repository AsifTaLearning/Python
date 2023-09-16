# strings

print("Hello")
print('Hello')

# Assign String to a Variable

a = "Hello"

print(a)

# Multiline Strings

a = """ blaaah blah bluuu blaaa
blii bluu blaaa blaaah blah bluuu 
blaaablii bluu blaaa. """ # double quotes

print(a)

# Another example

a = """ blaaah blah bluuu blaaa
blii bluu blaaa blaaah blah bluuu 
blaaablii bluu blaaa. """  # single quotes

print(a)

# Slicing 

b = "Hello, World!"

print(b[2:5])

# Slice From the Start

b = "Hello, World!"

print(b[:5])


# Slice To the End

b = "Hello, World!"

print(b[7:])

# Negative Indexing

b = "Hello, World!"

print(b[-5:-2])

# Modify Strings
# Upper Case

a = "Hello, World!"

print(a.upper())

# Lower Case

a = "Hello, World!"

print(a.lower())

# Remove Whitespace

a = "    Hello, World!    "

print(a.strip())

# Replace String

a = "Hello, World!"

print(a.replace("H","j"))

# Split String

a = "Hello,World!"

print(a.split(","))

# String Concatenation

a = "Hello"
b = "World"

c = a + b

print(c)

# Another example

a = "Hello"
b = "World"

c = a + " " + b

print(c)


# String Format

age = 36
txt = "My name is John, and I am {}"

print(txt.format(age))


# Another example

quantity = 3
itemno = 567
price = 49.95

myorder = "I want {} pieces of item {} for {} dollars."

print(myorder.format(quantity,itemno,price))

# Another problem

quantity = 3
itemno = 567
price = 49.95

myorder = "I want to pay {2} dollars for {0} pieces of item {1}."

print(myorder.format(quantity,itemno,price))

# Escape Character

txt = "blaah blu \"yohoo\" bla bluuu"

print(txt)

# Single Quote

txt = 'It\'s alright.'

print(txt) 
	
# Backslash

txt = "This will insert one \\ (backslash)."

print(txt) 

# New Line	

txt = "Hello\nWorld!"

print(txt) 

# Carriage Return	

txt = "Hello\rWorld!"

print(txt) 

# Tab	

txt = "Hello\tWorld!"

print(txt) 

# Backspace	

txt = "Hello \bWorld!" #This example erases one character 

print(txt) 

# 	Form Feed

txt = "Hello \fWorld!"

print(txt) 

# Octal value	

txt = "\110\145\154\154\157"

print(txt) 

# Hex value

txt = "\x48\x65\x6c\x6c\x6f"

print(txt) 

# String Methods
# Converts the first character to upper case

txt = "hello world!"

print(txt.capitalize()) 

# 	Converts string into lower case

txt = "HELLO WORLD!"

print(txt.casefold())

# Returns a centered string

txt = "Hello World!"

print(txt.center(10))

# 	Returns the number of times a specified value occurs in a string

txt = "Hello World Hello Hello!"

print(txt.count("Hello"))

# 	Returns an encoded version of the string

txt = "Hello World!"

print(txt.encode())

# Returns true if the string ends with the specified value

txt = "Hello World!"

print(txt.endswith("!"))

# Sets the tab size of the string

txt = "Hello World!"

print(txt.expandtabs())

# Searches the string for a specified value and returns the position of where it was found

txt = "Hello World!"

print(txt.find("W"))

# Formats specified values in a string

txt = "Hello World {}!"

print(txt.format("formated"))

# Another Formats specified values in a string

a = {'x':"john", 'y':'wick'}
  
print("{x}\'s last name is {y}".format_map(a))

# Searches the string for a specified value and returns the position of where it was found

txt = "Hello World!"

print(txt.index("o"))

# Returns True if all characters in the string are alphanumeric

txt = "123456"

print(txt.isalnum())

# Returns True if all characters in the string are in the alphabet

txt = "HelloWorld"

print(txt.isalpha())

# Returns True if all characters in the string are ascii characters

txt = "Hello World!"

print(txt.isascii())

# Returns True if all characters in the string are decimals

txt = "5637832"

print(txt.isdecimal())

# Returns True if all characters in the string are digits

txt = "098865"

print(txt.isdigit())

# Returns True if the string is an identifier

txt = "HelloWorld"

print(txt.isidentifier())

# Returns True if all characters in the string are lower case

txt = "hello world!"

print(txt.islower())

# Returns True if all characters in the string are numeric

txt = "5848554"

print(txt.isnumeric())

# Returns True if all characters in the string are printable

txt = "hello$#() world!"

print(txt.isprintable())

# Returns True if all characters in the string are whitespaces

txt = "      "

print(txt.isspace())

# 	Returns True if the string follows the rules of a title

txt = "Helloworld"

print(txt.istitle())

# Returns True if all characters in the string are upper case

txt ="HELLO WORLD!"

print(txt.isupper())

# Joins the elements of an iterable to the end of the string

txt = "Hello "

print(txt.join("yoho "))

# Returns a left justified version of the string

txt = "Hello World!"

print(txt.ljust(20)," man")

# 	Converts a string into lower case

txt = "Hello World!"

print(txt.lower())

# Returns a left trim version of the string

txt = "     Hello World!"

print(txt.lstrip())

# Returns a translation table to be used in translations

txt = "Hello World!"
my_table = str.maketrans("W","Y")

print(txt.translate(my_table))

# Returns a tuple where the string is parted into three parts

txt = "Hello World!"

print(txt.partition("lo W"))

# Returns a string where a specified value is replaced with a specified value

txt = "I like bananas"

x = txt.replace("bananas","apple")

print(x)

# Searches the string for a specified value and returns the last position of where it was found

txt = "Hello World!"

print(txt.rfind("o"))

# Searches the string for a specified value and returns the last position of where it was found

txt = "Hello World!"

print(txt.rindex("l"))

# Returns a right justified version of the string

txt = "Hello World!"

print(txt.rjust(20))

# Returns a tuple where the string is parted into three parts

txt = "Hello World!"

print(txt.rpartition("o Wo"))

# Splits the string at the specified separator, and returns a list

txt = "Hello , World!"

print(txt.rsplit(" , "))

# 	Returns a right trim version of the string

txt = "Hello World!      "

print(txt.rstrip())

# Splits the string at the specified separator, and returns a list

txt = "     2Hello Wor ld!      "

print(txt.split())

# Splits the string at line breaks and returns a list

txt = "Hello \n World!"

print(txt.splitlines())

# Returns true if the string starts with the specified value

txt = "Hello \n World!"

print(txt.startswith("H"))

# Returns a trimmed version of the string

txt = "     2Hello World!      "

print(txt.strip())

# Swaps cases, lower case becomes upper case and vice versa

txt = "Hello World!"

print(txt.swapcase())

# Converts the first character of each word to upper case

txt = "hello world!"

print(txt.title())

# Returns a translated string

mydict = {83:  80}  #use a dictionary with ascii codes to replace 83 (S) with 80 (P):
txt = "Hello Sam!"

print(txt.translate(mydict))

# Converts a string into upper case

txt = "hello world!"

print(txt.upper())

# Fills the string with a specified number of 0 values at the beginning

txt = "55"

x = txt.zfill(100)

print(x)






