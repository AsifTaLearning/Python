# Set

thisset = {"apple", "banana", "cherry"}

print(thisset)

# Duplicates Not Allowed

thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

# True and 1 is considered the same value:

thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)

# Get the Length of a Set

thisset = {"apple", "banana", "cherry"}

print(len(thisset))

# Set Items - Data Types

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

# Another example

set1 = {"abc", 34, True, 40, "male"}

# type()

myset = {"apple", "banana", "cherry"}

print(type(myset))

# The set() Constructor

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets

print(thisset)

# Access Set Items

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  
  print(x)

# Another example

thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)

# Add Set Items
# Add item

thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

# Add Sets

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

# Add Any Iterable

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)

# Remove Set Items
# Remove Item

thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

# Another example

thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)

# Another example

thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)

# Another example

thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)

# Another example

thisset = {"apple", "banana", "cherry"}

del thisset

# loop sets
# Loop Items

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)


# Join Sets
# Join Two Sets

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)

print(set3)

# Another example

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

# Another example

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

# Keep ONLY the Duplicates

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)

# Another example

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)

# Keep All, But NOT the Duplicates

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)

# Another example

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z)

# Another example

x = {"apple", "banana", "cherry", True}
y = {"google", 1, "apple", 2}

z = x.symmetric_difference(y)

print(z)

# Adds an element to the set

fruits = {"apple", "banana", "cherry"}

fruits.add("orange")

print(fruits)

# Removes all the elements from the set

fruits = {"apple", "banana", "cherry"}

fruits.clear()

print(fruits)

# Returns a copy of the set

fruits = {"apple", "banana", "cherry"}

x = fruits.copy()

print(x)

# Returns a set containing the difference between two or more sets

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.difference(y)

print(z)

# 	Removes the items in this set that are also included in another, specified set

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.difference_update(y)

print(x)

# Remove the specified item

fruits = {"apple", "banana", "cherry"}

fruits.discard("banana")

print(fruits)

# Returns a set, that is the intersection of two other sets

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)

# Removes the items in this set that are not present in other, specified set(s)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)

# Returns whether two sets have a intersection or not

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}

z = x.isdisjoint(y)

print(z)

#  Returns whether another set contains this set or not

x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}

z = x.issubset(y)

print(z)

# Returns whether this set contains another set or not

x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}

z = x.issuperset(y)

print(z)

# Removes an element from the set

fruits = {"apple", "banana", "cherry"}

fruits.pop()

print(fruits)

# Removes the specified element

fruits = {"apple", "banana", "cherry"}

fruits.remove("banana")

print(fruits)

# Returns a set with the symmetric differences of two sets

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z)

# inserts the symmetric differences from this set and another

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)

# Return a set containing the union of sets

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.union(y)

print(z)

# Update the set with the union of this set and others

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.update(y)

print(x)






