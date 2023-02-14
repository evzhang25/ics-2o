"""
INTRO TO VARIABLES AND INPUT
Goal:
Create simple programs with two or more variables
and output some result

Get user input and convert to integer.
"""

# Assigning values to variables
# -----------------------------
# Think of variables as a container
# ex:   assign 5 to variable a,
#       assign 7 to variable b,
#       assign the sum of a and b to variable c
a = 5
b = 7
c = a + b
print(456) # print a literal number
print("Hello, world! This is a string!") # print a literal string
print(c) # print a variable's value
print() # print a new line

# EXAMPLE 01:
# Program that will store a price and a quantity.
# calculate subtotal, tax, total
# print those out separately
# multiplication - *

price = 5.99
quantity = 5
subtotal = price * quantity
tax = subtotal * 0.13
total = subtotal + tax
print(round(subtotal, 2))
print(round(tax, 2))
print(round(total, 2))