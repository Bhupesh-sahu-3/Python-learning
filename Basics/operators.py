

#standard divison operation, returns a float even if both operands are integers
print(5/2); # returns 2.5, as the result is a float
print(4/2); # returns 2.0, as the result is a float

#integer division operation, returns the quotient as an integer by discarding the decimal part
print(5//2); # returns 2, as the decimal part is discarded
print(4//2); # returns 2, as the decimal part is discarded

# modulus operator returns the remainder of the division
print(5%2); # returns 1, as 5 divided by 2 leaves a remainder of 1
print(4%2); # returns 0, as 4 divided by 2 leaves no remainder

#power operator returns the result of the first operand raised to the power of the second operand
print(2**3); # returns 8, as 2 raised to the power of 3 is 8
print(3**2); # returns 9, as 3 raised to the power of 2 is 9        


# Note that the floor division operator (//) behaves differently when one or both operands are floats.
#  It returns the largest integer less than or equal to the result of the division, which can be a float if either operand is a float.
6 // 3     # returns 2
6.0 // 3   # returns 2.0
6 // 3.0   # returns 2.0
6.0 // 3.0 # returns 2.0

#Division by zero raises a ZeroDivisionError
# print(5/0) # raises ZeroDivisionError: division by zero   


#short hand assignment operators
x = 5
x += 3 # equivalent to x = x + 3, now x is 8    
x -= 2 # equivalent to x = x - 2, now x is 6
x *= 4 # equivalent to x = x * 4, now x is 24
x /= 6 # equivalent to x = x / 6, now x is 4.0
x //= 2 # equivalent to x = x // 2, now x is 2.0
x %= 2 # equivalent to x = x % 2, now x is 0
x **= 3 # equivalent to x = x ** 3, now x is 0


