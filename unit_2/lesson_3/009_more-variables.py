store = "No Frills"
item = "Apples"
price = 0.5
quantity = 7
subtotal = price * quantity
tax = subtotal * 0.13
total = tax + subtotal

print(f"At {store} I bought some {item}.")                                          # f-string
print("They sold for $" + str(round(price, 2)) + " each.")                          # concatenation
print("I wanted to purchase {} of them.".format(quantity))                          # "dot format"
print(f"The subtotal is ${round(subtotal, 2)}; thus, the tax is ${round(tax, 2)}")  # f-string
print(f"The total price, with tax included, was ${round(total, 2)}.")               # f-string

# 1.    The last line was not printed properly because it wasn't a f-string