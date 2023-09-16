# Boolean Values

print(10 > 9)
print(10 == 9)
print(10 < 9)


# Another example

a = 200
b = 33

if b > a:
  
  print("b is greater than a")

else:
  
  print("b is not greater than a")

# Evaluate Values and Variables

print(bool("Hello"=="Hello"))
print(bool(15 == 15))

# Another example

x = "Hello"
y = 15

print(bool(x))
print(bool(y))

# Most Values are True

x = bool("abc")
print(x)

x = bool(123)
print(x)

x = bool(["apple", "cherry", "banana"])
print(x)



# Some Values are False

x = bool(False)
print(x)

x = bool(None)
print(x)

x = bool(0)
print(x)

x = bool("")
print(x)

x = bool(())
print(x)

x = bool([])
print(x)

x = bool({})
print(x)

# Another example

class myclass():
  
  def __len__(self):

    return 0

myobj = myclass()

print(bool(myobj))

# Functions can Return a Boolean

def myFunction() :
  
  return True

print(myFunction())

# Another example

def myFunction() :
  
  return True

if myFunction():
  
  print("YES!")

else:
  
  print("NO!")

# Another example

x = 200

print(isinstance(x, int))



