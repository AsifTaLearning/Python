import random


# Numbers

x = 1    # int
y = 2.8  # float
z = 1j   # complex

print(type(x))
print(type(y))
print(type(z))



# int

x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))


# Float

x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

# Another example
                
x = 35e3     # Float can also be scientific numbers with an "e" to indicate the power of 10.
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))


# Complex

x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))


# Type Conversion

x = 1    # int
y = 2.8  # float
z = 1j   # complex

a = float(x) #convert from int to float:
b = int(y) #convert from float to int:
c = complex(x) #convert from int to complex:

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

# Random Number

x = random.randrange(1,10)

print(x)
