# 11-5. 5-Star Meal

menu = {"burger": 7.99, "pizza": 9.99, "cookie": 1.25}
total_price = 0

# Since my menu is only 3 items, we could take the sum of the prices
# But let's pretend it's not the whole menu haha
# print(sum(menu.values()))

total_price += menu['burger']
total_price += menu['pizza']
total_price += menu['cookie']

print(f'You ordered a burger, pizza, and cookie. The total comes out to be ${total_price}.')

# After the exercises, we learned about iterating over dictionaries
# Just in case you wanted to see this!

food_items = list(menu.keys())[:3] # menu.keys() gets a dict_keys object. Since indexing doesn't work on that type of data, we want to treat it like a list. 
prices = list(menu.values())[:3] 
total_price_2 = sum(prices)
# total_price_2 = sum(menu[item] for item in ordered_items) # if you know comprehension
print(f"You ordered a {food_items[0]}, {food_items[1]}, and {food_items[2]}. The total comes out to be ${total_price_2}.")

