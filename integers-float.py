num = 4.71

print(type(num))  # Output: <class 'float'>

# Arithmetic Operations
# print(5 + 3)      # Addition: Output: 8
# print(5 - 3)      # Subtraction: Output: 2
# print(5 * 3)      # Multiplication: Output: 15
# print(5 / 2)      # Division: Output: 2.5   
# print(5 // 2)     # Floor Division: Output: 2
# print(5 % 2)      # Modulus: Output: 1
# print(5 ** 2)     # Exponentiation: Output: 25


# Absolute Value
print(abs(-7))    # Output: 7 
print(round(3.62, 2))  # Output: 3.62

# Python uses "bankers' rounding" for .5 cases i.e rounds half to the nearest even number
print(round(2.5)) # Output: 2
print(round(3.5)) # Output: 4 
print(round(3.65, 1))  # Output: 3.6
print(round(4.75, 1))  # Output: 4.8



# Comparing Numbers
# Equal: print(5 == 5)      # Output: True
# Not Equal: print(5 != 3)  # Output: True
# Greater Than: print(5 > 3) # Output: True
# Less Than: print(3 < 5)    # Output: True
# Greater Than or Equal To: print(5 >= 5) # Output: True
# Less Than or Equal To: print(3 <= 5)    # Output: True


num_1 = '100'
num_2 = '200'

print(num_1 + num_2)  # Output: '100200' (string concatenation)

# Casting Strings to Numbers
num_1 = int(num_1)
num_2 = int(num_2)

print(num_1 + num_2)  # Output: 300 (integer addition)
