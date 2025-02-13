# 10-8. Average Menu Price

menu = {"burger": 7.99, "pizza": 9.99, "cookie": 1.25}

total_price = sum(menu.values()) # menu.values() returns a dict_values. That is considered an iterable which sum() happily takes.
avg_price = total_price / len(menu)

print(f"The average menu price is ${avg_price}.")