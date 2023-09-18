# Tuple

thistuple = ("apple", "banana", "cherry")

print(thistuple)

# Tuple Length

thistuple = ("apple", "banana", "cherry")

print(len(thistuple))

# Create Tuple With One Item

thistuple = ("apple",)

print(type(thistuple))

thistuple = ("apple")  #NOT a tuple

print(type(thistuple))

# Tuple Items - Data Types

tuple1 = ("apple", "banana", "cherry",3)
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

print(tuple1)
print(tuple2)
print(tuple3)

# Another example

tuple1 = ("abc", 34, True, 40, "male")

print(tuple1)

# type()

mytuple = ("apple", "banana", "cherry")

print(type(mytuple))

# The tuple() Constructor

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets

print(thistuple)

# Access Tuple Items

thistuple = ("apple", "banana", "cherry")

print(thistuple[1])

# Another example

thistuple = ("apple", "banana", "cherry")

print(thistuple[-1])

# Another example

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")

print(thistuple[2:5])

# Another example

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")

print(thistuple[:4])

# Another example

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")

print(thistuple[2:])

# Another example

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")

print(thistuple[-4:-1])

# Check if Item Exists

thistuple = ("apple", "banana", "cherry")

if "apple" in thistuple:
  
  print("Yes, 'apple' is in the fruits tuple")

# Update Tuples
# Change Tuple Values

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

# Add Items

thistuple = ("apple", "banana", "cherry")

y = list(thistuple)

y.append("orange")

thistuple = tuple(y)

# Add tuple to a tuple

thistuple = ("apple", "banana", "cherry")

y = ("orange",)

thistuple += y

print(thistuple)

# Remove Items

thistuple = ("apple", "banana", "cherry")

y = list(thistuple)

y.remove("apple")

thistuple = tuple(y)

# thistuple = ("apple", "banana", "cherry")

del thistuple

# Unpacking a Tuple

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

# Using Asterisk*

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

# Another example

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

# Loop Tuples
# Loop Through a Tuple

thistuple = ("apple", "banana", "cherry")

for x in thistuple:
  
  print(x)

# Loop Through the Index Numbers

thistuple = ("apple", "banana", "cherry")

for i in range(len(thistuple)):
  
  print(thistuple[i])

# Using a While Loop

thistuple = ("apple", "banana", "cherry")

i = 0
while i < len(thistuple):
  
  print(thistuple[i])

  i = i + 1

# Join Tuples
# Join Two Tuples

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2

print(tuple3)

# Multiply Tuples

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)

# Tuple Methods

# Returns the number of times a specified value occurs in a tuple

thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.count(5)

print(x)

# Searches the tuple for a specified value and returns the position of where it was found

thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.index(8)

print(x)

