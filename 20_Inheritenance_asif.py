# Create a Parent Class

class Person:
  
  def __init__(self, fname, lname):

    self.firstname = fname
    self.lastname = lname

  def printname(self):

    print(self.firstname, self.lastname)

x = Person("John", "Doe")

x.printname()

# Create a Child Class

class Student(Person):
  
  pass

# class Person:

  def __init__(self, fname, lname):

    self.firstname = fname
    self.lastname = lname

  def printname(self):

    print(self.firstname, self.lastname)

class Student(Person):
  
  pass

x = Student("Mike", "Olsen")

x.printname()

# Add the __init__() Function

class Person:
  
  def __init__(self, fname, lname):

    self.firstname = fname
    self.lastname = lname

  def printname(self):

    print(self.firstname, self.lastname)

class Student(Person):
  
  def __init__(self, fname, lname):

    Person.__init__(self, fname, lname)

x = Student("Mike", "Olsen")

x.printname()

# Use the super() Function

class Person:
  
  def __init__(self, fname, lname):
    
    self.firstname = fname
    self.lastname = lname

  def printname(self):

    print(self.firstname, self.lastname)

class Student(Person):
  
  def __init__(self, fname, lname):

    super().__init__(fname, lname)

x = Student("Mike", "Olsen")

x.printname()

# Add Properties

class Person:
  
  def __init__(self, fname, lname):

    self.firstname = fname
    self.lastname = lname

  def printname(self):

    print(self.firstname, self.lastname)

class Student(Person):
  
  def __init__(self, fname, lname):

    super().__init__(fname, lname)

    self.graduationyear = 2019

x = Student("Mike", "Olsen")

print(x.graduationyear)

# Another example

class Person:
  
  def __init__(self, fname, lname):
    
    self.firstname = fname
    self.lastname = lname

  def printname(self):

    print(self.firstname, self.lastname)

class Student(Person):
  
  def __init__(self, fname, lname, year):

    super().__init__(fname, lname)

    self.graduationyear = year

x = Student("Mike", "Olsen", 2019)

print(x.graduationyear)

# Add Methods

class Person:
  
  def __init__(self, fname, lname):

    self.firstname = fname
    self.lastname = lname

  def printname(self):

    print(self.firstname, self.lastname)

class Student(Person):
  
  def __init__(self, fname, lname, year):

    super().__init__(fname, lname)

    self.graduationyear = year

  def welcome(self):

    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen", 2019)

x.welcome()







