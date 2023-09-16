# Built-in Data Types
# Text Type: str

x = "hello"  # str

print(type(x))


# Numeric Types:	int, float, complex

x1 = 3
x2 = 3.0
x3 = 3j

print(type(x1))  # int
print(type(x2))  # float
print(type(x3))  # complex


# Sequence Types:	list, tuple, range

x1 = ["a","b","c"] # list
x2 = ("d","e","f") # tupil
x3 = range(6)      # range

print(type(x1))
print(type(x2))
print(type(x3))


# Mapping Type:	dict

x = {
    "name" : "tintu" , # dic
    "age" : 12 
}

print(type(x))


# Set Types:	set, frozenset

x1 = {"a","b","c"}   # set
x2 = ({"a","b","c"}) # frozenset

print(type(x1))
print(type(x2))


# Boolean Type:	bool

x1 = True # bool
x2 = False

print(type(x1))
print(type(x2))

# Binary Types:	bytes, bytearray, memoryview

x1 = b"hello"             # bytes
x2 = bytearray(6)         # bytearray
x3 = memoryview(bytes(5)) # memoryview

print(type(x1))
print(type(x2))
print(x3)


# None Type:	NoneType

x = None # NoneType

print(x)


# Setting the Specific Data Type

x = str("Hello World")	                      # str	
print("str = "+str(x))

x = int(20)	                                  # int	
print("int = "+str(x))

x = float(20.5)	                              # float	
print("float = "+str(x))

x = complex(1j)                               # complex	
print("complex = "+str(x))

x = list(("apple", "banana", "cherry"))	      # list	
print("list = "+str(x))

x = tuple(("apple", "banana", "cherry"))	  # tuple	
print("tuple = "+str(x))

x = range(6)	                              # range	
print("range = "+str(x))

x = dict(name="John", age=36)	              # dict	
print("dict = "+str(x))

x = set(("apple", "banana", "cherry"))	      # set	
print("set = "+str(x))

x = frozenset(("apple", "banana", "cherry"))  # frozenset	
print("frozenset = "+str(x))

x = bool(5)                                   # bool	
print("bool = "+str(x))

x = bytes(5)                                  # bytes	
print("bytes = "+str(x))

x = bytearray(5)                              # bytearray	
print("bytearray = "+str(x))

x = memoryview(bytes(5))                      # memoryview
print("memoryview = "+str(x))


