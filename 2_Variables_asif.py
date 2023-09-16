# Creating Variables

x = 5
y = "John"

print(x)
print(y)


# Another example

x = 4       # x is of type int
x = "Sally" # x is now of type str

print(x)


# Casting

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0


# Get the type

x = 5
y = "John"

print(type(x))
print(type(y))


# Single or Double Quotes?

x = "John"

    # is the same as

x = 'John'


# Case-Sensitive

a = 4
A = "Sally"   #A will not overwrite a


# Variable Names

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"


# Many Values to Multiple Variables

x ,y ,z = "banana ","apple" ,"grapes"

print(x)
print(y)
print(z)


# One Value to Multiple Variables

x = y = z = "fruits"

print(x)
print(y)
print(z)


# Unpack a Collection

fruits = "grapes", "apple",  "banana"

x ,y ,z = fruits

print(x)
print(y)
print(z)


# Output Variables

x = "Python is awesome"

print(x)


# Another example

x = "Python"
y = "is"
z = "awesome"

print(x, y, z)


# Another example

x = "Python "
y = "is "
z = "awesome"

print(x + y + z)


# Another example

x = 5
y = 10

print(x + y)


# Another example

x = 5
y = "John"

print(x, y)


# Global Variables

x = "awesome"

def f():

    print("python is "+str(x))

f()


# Another example

x = "awesome"

def myfunc():
  
  x = "fantastic"

  print("Python is " + x)

myfunc()

print("Python is " + x)


# The global Keyword

def myfunc():
  
  global x
  x = "great"

myfunc()

print("Python is " + x)


# Another problem

x = "great"

def myfunc():
  
  global x 
  x = "good"

myfunc()

print("Python is " + x)

# 

