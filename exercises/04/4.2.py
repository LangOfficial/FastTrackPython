# 4-2. How Much Money Did I Save?

cart_total = 0
discount = .3

# Add items to the cart
cart_total += 12.99
cart_total += 9.99
cart_total += .99

saved_money = cart_total * discount

print(f"I saved ${saved_money}!")