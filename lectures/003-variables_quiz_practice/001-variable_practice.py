# Ask the user how many apples they picked.
# Each apple weighs 80 grams on average.
# The price for apples is $1.99 per kilogram.
# What is the price including tax for the apples they picked?

AVERAGE_WEIGHT = 0.08
PRICE_PER_KILO = 199 # in cents
TAX_RATE = 0.13

apples = int(input("How many apples are you buying? "))
weight = apples * AVERAGE_WEIGHT

subtotal = PRICE_PER_KILO * weight
tax = subtotal * TAX_RATE
total = round(subtotal + tax)

print(f"The cost of {apples} apples including tax is ${total // 100}.{total % 100}")