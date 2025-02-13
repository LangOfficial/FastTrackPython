# 10-5. 5-Star Meal

menu = {"burger": 7.99, "pizza": 9.99, "cookie": 1.25}
total_price = 0

# since my menu is only 3 items, we could take the sum of the prices
# but let's pretend it's not the whole menu haha
# print(sum(menu.values()))

total_price += menu['burger']
total_price += menu['pizza']
total_price += menu['cookie']

print(f'You ordered a burger, pizza, and cookie. The total comes out to be ${total_price}.')

# after the exercises, we learned about iterating over dictionaries
# just in case you wanted to see this!
food_items = list(menu.keys()) # menu.keys() gets a dict_keys object. Since indexing doesn't work on it, we want to treat it like a list. 
print(f"You ordered a {food_items[0]}, {food_items[1]}, and {food_items[2]}. The total comes out to be ${total_price}.")

