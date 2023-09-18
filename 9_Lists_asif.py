# python List

mylist = ["apple", "banana", "cherry"]

# List

thislist = ["apple", "banana", "cherry"]

print(thislist)

# Allow Duplicates

thislist = ["apple", "banana", "cherry", "apple", "cherry"]

print(thislist)

# List Length

thislist = ["apple", "banana", "cherry"]

print(len(thislist))

# List Items - Data Types

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

print(list1)
print(list2)
print(list3)

# Another example

list1 = ["abc", 34, True, 40, "male"]

print(list1)

# type()

mylist = ["apple", "banana", "cherry"]

print(type(mylist))

# The list() Constructor

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets

print(thislist)

# Access Items

thislist = ["apple", "banana", "cherry"]

print(thislist[1])

# Another example

thislist = ["apple", "banana", "cherry"]

print(thislist[-1])

# Another example

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

print(thislist[2:5])

# Another example

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

print(thislist[:4])

# Another example

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

print(thislist[2:])

# Another example

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

print(thislist[-4:-1])

# Check if Item Exists

thislist = ["apple", "banana", "cherry"]

if "apple" in thislist:
  
  print("Yes, 'apple' is in the fruits list")

# Change Item Value

thislist = ["apple", "banana", "cherry"]

thislist[1] = "blackcurrant"

print(thislist)

# Change a Range of Item Values

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]

thislist[1:3] = ["blackcurrant", "watermelon"]

print(thislist)

# Another example

thislist = ["apple", "banana", "cherry"]

thislist[1:2] = ["blackcurrant", "watermelon"]

print(thislist)

# Another example

thislist = ["apple", "banana", "cherry"]

thislist[1:3] = ["watermelon"]

print(thislist)

# Insert Items

thislist = ["apple", "banana", "cherry"]

thislist.insert(2, "watermelon")

print(thislist)

#  Add List Items
# Append Items

thislist = ["apple", "banana", "cherry"]

thislist.append("orange")

print(thislist)

# Insert Items

thislist = ["apple", "banana", "cherry"]

thislist.insert(1, "orange")

print(thislist)

# Extend List

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]

thislist.extend(tropical)

print(thislist)

# Add Any Iterable

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")

thislist.extend(thistuple)

print(thislist)

# Remove List Items
# Remove Specified Item

thislist = ["apple", "banana", "cherry"]

thislist.remove("banana")

print(thislist)

# Remove the first occurance of "banana"

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]

thislist.remove("banana")

print(thislist)

# Remove Specified Index

thislist = ["apple", "banana", "cherry"]

thislist.pop(1)

print(thislist)

# Remove the last item:

thislist = ["apple", "banana", "cherry"]

thislist.pop()

print(thislist)

# Remove the first item:

thislist = ["apple", "banana", "cherry"]

del thislist[0]

print(thislist)

# Delete the entire list:

thislist = ["apple", "banana", "cherry"]

del thislist

# Clear the List

thislist = ["apple", "banana", "cherry"]

thislist.clear()

print(thislist)

# Loop Lists

thislist = ["apple", "banana", "cherry"]

for x in thislist:
  
  print(x)

# Loop Through the Index Numbers

thislist = ["apple", "banana", "cherry"]

for i in range(len(thislist)):
  
  print(thislist[i])

# Using a While Loop

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  
  print(thislist[i])

  i = i + 1

# Looping Using List Comprehension

thislist = ["apple", "banana", "cherry"]

[print(x) for x in thislist]

# List Comprehension

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  
  if "a" in x:

    newlist.append(x)

print(newlist)

# Another example

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

# Another example

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if x != "apple"]

print(newlist)

# Another example

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits]

print(newlist)

# Another example

newlist = [x for x in range(10)]

print(newlist)

# Another example

newlist = [x for x in range(10) if x < 5]

print(newlist)

# Another example

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x.upper() for x in fruits]

print(newlist)

# Another example 

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = ['hello' for x in fruits]

print(newlist)

# Another example

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x if x != "banana" else "orange" for x in fruits]

print(newlist)

# Sort list
# Sort List Alphanumerically

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]

thislist.sort()

print(thislist)

# thislist = [100, 50, 65, 82, 23]

thislist.sort()

print(thislist)

# Sort Descending

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]

thislist.sort(reverse = True)

print(thislist)

# Another example

thislist = [100, 50, 65, 82, 23]

thislist.sort(reverse = True)

print(thislist)

# Customize Sort Function

def myfunc(n):
  
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]

thislist.sort(key = myfunc)

print(thislist)

# Case Insensitive Sort

thislist = ["banana", "Orange", "Kiwi", "cherry"]

thislist.sort()

print(thislist)

# Another example

thislist = ["banana", "Orange", "Kiwi", "cherry"]

thislist.sort(key = str.lower)

print(thislist)

# Reverse Order

thislist = ["banana", "Orange", "Kiwi", "cherry"]

thislist.reverse()

print(thislist) 

# Copy list

thislist = ["apple", "banana", "cherry"]

mylist = thislist.copy()
print(mylist)

# Another example

thislist = ["apple", "banana", "cherry"]

mylist = list(thislist)

print(mylist)

# Join Lists
# Join Two Lists

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2

print(list3)

# Append list2 into list1:

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:

  list1.append(x)

print(list1)

# Use the extend() method to add list2 at the end of list1:

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)

print(list1)

# List Methods
# Adds an element at the end of the list

fruits = ['apple', 'banana', 'cherry']

fruits.append("orange")

print(fruits)

# Removes all the elements from the list

fruits = ['apple', 'banana', 'cherry', 'orange']

fruits.clear()

print(fruits)

# Returns a copy of the list

fruits = ['apple', 'banana', 'cherry', 'orange']

x = fruits.copy()

print(x)

# Returns the number of elements with the specified value

fruits = ['apple','cherry', 'banana', 'cherry']

x = fruits.count("cherry")

print(x)

# Add the elements of a list (or any iterable), to the end of the current list

fruits = ['apple', 'banana', 'cherry']

cars = ['Ford', 'BMW', 'Volvo']

fruits.extend(cars)

print(fruits)

# Returns the index of the first element with the specified value

fruits = ['apple', 'banana', 'cherry']

x = fruits.index("cherry")

print(x)

# Adds an element at the specified position

fruits = ['apple', 'banana', 'cherry']

fruits.insert(1, "orange")

print(fruits)

# Removes the element at the specified position

fruits = ['apple', 'banana', 'cherry']

fruits.pop(1)

print(fruits)

# Removes the item with the specified value

fruits = ['apple', 'banana', 'cherry']

fruits.remove("banana")

print(fruits)

# Reverses the order of the list

fruits = ['apple', 'banana', 'cherry']

fruits.reverse()

print(fruits)

# Sorts the list

cars = ['Ford', 'BMW', 'Volvo']

cars.sort()

print(cars)

# 