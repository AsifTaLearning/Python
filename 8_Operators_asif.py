from sympy import var

# Arithmetic Operators

print(10 + 5)

# Addition

x = 20
y = 10

print(x + y)

# Subtraction

x = 20
y = 10

print(x - y)

# Multiplication

x = 20
y = 10

print(x * y)

# Division

x = 20
y = 10

print(x / y)

# Modulus

x = 20
y = 10

print(x % y)

# Exponentiation

x = 20
y = 10

print(x ** y)

# Floor division

x = 20
y = 10

print(x // y)

# Assignment Operators
# x = 5

x = 5

print(x)

# 	x = x + 3	

x =5
x += 3

print(x)

# x = x - 3

x =5
x -= 3

print(x)

# 	x = x * 3	

x=5
x *= 3

print(x)

# x = x / 3

x = 5
x /= 3

print(x)

# x = x % 3
	
x = 5
x %= 3

print(x)

# 	x = x // 3	

x = 5
x//=3

print(x)

# x = x ** 3

x = 5
x **= 3

print(x)

# 	x = x & 3

x = 5
x &= 3

print(x)

# x = x | 3

x = 5
x |= 3

print(x)

# x = x ^ 3

x = 5
x ^= 3

print(x)

# x = x >> 3

x = 5
x >>= 3

print(x)

# x = x << 3

x = 5
x <<= 3

print(x)

# Comparison Operators
# Equal	

x == y

# Not equal	

x != y

# 	Greater than	

x > y

#  Less than

x < y

# Greater than or equal to	

x >= y

# 	Less than or equal to	

x <= y

# Logical Operators
# Returns True if both statements are true	

x < 5 and  x < 10

# Returns True if one of the statements is true	

x < 5 or x < 4

# Reverse the result, returns False if the result is true	

not(x < 5 and x > 4)

# Identity Operators
# Returns True if both variables are the same object	

x is y

# Returns True if both variables are not the same object	

x is not y

# Membership Operators
# Returns True if a sequence with the specified value is present in the object	
x = 5
y = [2,3,4,5]

x in y

# 	Returns True if a sequence with the specified value is not present in the object

x not in y

# Bitwise Operators
# AND Sets each bit to 1 if both bits are 1

print(6 & 3)

# OR , Sets each bit to 1 if one of two bits is 1	

print(6 | 3)

# XOR  , Sets each bit to 1 if only one of two bits is 1

print(6 ^ 3)

# NOT ,Inverts all the bits

print(~3)

# Zero fill left shift	, Shift left by pushing zeros in from the right and let the leftmost bits fall off

print(3 << 2)

# Signed right shift ,	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off

print(8 >> 2)

# Operator Precedence

print((6 + 3) - (6 + 3))

# Another example

print(100 + 5 * 3)

# Parentheses

print((6 + 3) - (6 + 3))

# Exponentiation

print(100 - 3 ** 3)

# Unary plus, unary minus, and bitwise NOT

print(100 + ~3)

# Multiplication, division, floor division, and modulus

print(100 + 5 * 3)

# Addition and subtraction

print(100 - 5 * 3)

# Bitwise left and right shifts

print(8 >> 4 - 2)

# Bitwise AND

print(6 & 2 + 1)

# Bitwise XOR

print(6 ^ 2 + 1)

# Bitwise OR

print(6 | 2 + 1)

# Comparisons, identity, and membership operators

print(5 == 4 + 1)

# Logical NOT

print(not 5 == 5)

# AND

print(1 or 2 and 3)

# OR

print(4 or 5 + 10 or 8)

# Another example

print(5 + 4 - 7 + 3)

