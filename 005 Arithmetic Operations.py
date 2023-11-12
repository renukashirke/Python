import math
print(math.ceil(2.9))
print(math.floor(2.9))

# +
# -
# *
# / - returns a float
# // - returns an int
# % - returns the remainder of division
# ** - exponentiation - x ** y = x to the power of y

# Augmented assignment operator:

x = 10

x = x + 10
print(x)

x += 10
print(x)

# Operator precedence:
# 1. parenthesis
# 2. exponentiation
# 3. multiplication / division
# 4. addition / subtraction

x = (2 + 3) * 10 - 3
print(x)

x = 2.9
print(round(x))

print(abs(-2.9))  # always returns a positive number
