# Python Lambda

x = lambda a : a + 10

print(x(5))

# Another example

x = lambda a, b : a * b

print(x(5, 6))

# Another example

x = lambda a, b, c : a + b + c

print(x(5, 6, 2))

# Why Use Lambda Functions?

def myfunc(n):
  
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

# Another example

def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(11))

# Another example

def myfunc(n):
  
  return lambda a : a * n

mydoubler = myfunc(2)

mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))


