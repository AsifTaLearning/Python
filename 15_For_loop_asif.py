# For Loops

fruits = ["apple", "banana", "cherry"]

for x in fruits:
  
  print(x)

# Looping Through a String

for x in "banana":
  
  print(x)

# The break Statement

fruits = ["apple", "banana", "cherry"]

for x in fruits:
  
  print(x)

  if x == "banana":

    break
  
# The continue Statement

fruits = ["apple", "banana", "cherry"]

for x in fruits:
  
  if x == "banana":

    continue
  
  print(x)

# The range() Function

for x in range(6):
  
  print(x)

# Another example

for x in range(2, 6):
  
  print(x)

# Another example

for x in range(2, 30, 3):
  
  print(x)

# Else in For Loop

for x in range(6):
  
  print(x)

else:
  
  print("Finally finished!")

# Another example

for x in range(6):
  
  if x == 3: break

  print(x)

else:
  
  print("Finally finished!")

# Nested Loops

adj = ["red", "big", "tasty"]

fruits = ["apple", "banana", "cherry"]

for x in adj:
  
  for y in fruits:

    print(x, y)

# The pass Statement

for x in [0, 1, 2]:
  
  pass
