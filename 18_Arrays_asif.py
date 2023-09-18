# Arrays

cars = ["Ford", "Volvo", "BMW"]

print(cars)

# Access the Elements of an Array

cars = ["Ford", "Volvo", "BMW"]

x = cars[0]

print(x)


# Another example

cars = ["Ford", "Volvo", "BMW"]

cars[0] = "Toyota"

print(cars)

# The Length of an Array

cars = ["Ford", "Volvo", "BMW"]

x = len(cars)

print(x)

# Looping Array Elements

cars = ["Ford", "Volvo", "BMW"]

for x in cars:
  
  print(x)

# Adding Array Elements

cars = ["Ford", "Volvo", "BMW"]

cars.append("Honda")

print(cars)

# Removing Array Elements

cars = ["Ford", "Volvo", "BMW"]

cars.pop(1)

print(cars)

# Another example

cars = ["Ford", "Volvo", "BMW"]

cars.remove("Volvo")

print(cars)

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

fruits = ['apple', 'banana', 'cherry']

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

# Removes the first item with the specified value

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









