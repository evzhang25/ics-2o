"""
Word problem:
David is going shopping and he will be purchasing exactly three items.
Ask him how much the items cost so you can tell him how much he will be spending.
Do this using a loop.

1.  Use a for loop to print out all the numbers from 0 to 10 inclusive.
2.  Create a while loop that does the same.
3.  Create a loop that says "hello" 5 times.
4.  Ask the user for three numbers and add them together using a loop.
"""

# PART 1
for i in range(0, 10):
    print(i + 1)
print()

# PART 2
a = 1
while a <= 10:
    print(a)
    a += 1
print()

# PART 3
for i in range(0, 5):
    print("hello")
print()

# PART 4
sum = 0.00
for i in range(0, 3):
    cost = float(input(f"Input cost of item {i + 1}: "))
    sum += cost
print(f"The total price is ${round(sum, 2)} before tax.")
print(f"The total price after tax is ${round(sum * 1.13, 2)}.")