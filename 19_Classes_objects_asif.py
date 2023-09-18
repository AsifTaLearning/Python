# Create a Class

class MyClass:
  
  x = 5

print(MyClass)

# Create Object

class MyClass:
  
  x = 5

p1 = MyClass()

print(p1.x)

# The __init__() Function

class Person:
  
  def __init__(self, name, age):

    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

# The __str__() Function

class Person:
  
  def __init__(self, name, age):

    self.name = name
    self.age = age

  def __str__(self):

    return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1)

# Object Methods

class Person:
  
  def __init__(self, name, age):

    self.name = name
    self.age = age

  def myfunc(self):

    print("Hello my name is " + self.name)

p1 = Person("John", 36)

p1.myfunc()

# The self Parameter

class Person:
  
  def __init__(mysillyobject, name, age):

    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):

    print("Hello my name is " + abc.name)

p1 = Person("John", 36)

p1.myfunc()

# Modify Object Properties

class Person:
  
  def __init__(self, name, age):

    self.name = name
    self.age = age

  def myfunc(self):

    print("Hello my name is " + self.name)

p1 = Person("John", 36)

p1.age = 40

print(p1.age)

# Delete Object Properties

class Person:
  
  def __init__(self, name, age):

    self.name = name
    self.age = age

  def myfunc(self):

    print("Hello my name is " + self.name)

p1 = Person("John", 36)

del p1.age

# Delete Objects

class Person:
  
  def __init__(self, name, age):

    self.name = name
    self.age = age

  def myfunc(self):
    
    print("Hello my name is " + self.name)

p1 = Person("John", 36)

del p1

# The pass Statement

class Person:
  
  pass





